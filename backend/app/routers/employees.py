from app.utils.employee import map_employee_to_schema
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse

from app import model
from app.database import get_db
from app.enum import UserType
from app.schemas import employee as employee_schema
from app.schemas.user import UserBase
from app.utils.auth import get_admin_user

router = APIRouter()


@router.post("/employees/", response_model=employee_schema.Employee)
def create_new_employee(
    payload: employee_schema.EmployeeCreate,
    db: Session = Depends(get_db),
):
    existing_user = db.query(model.User).filter(model.User.email == payload.email).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = model.User(
        username=payload.username,
        email=payload.email,
        user_type=UserType.EMPLOYEE.value
    )

    employee = model.Employee(
        first_name=payload.first_name,
        last_name=payload.last_name,
        employee_type=payload.employee_type,
        number_of_leaves=payload.number_of_leaves,
        benefits=payload.benefits,
        contract_end_date=payload.contract_end_date,
        project=payload.project,
        user=user
    )

    db.add(employee)
    db.commit()
    db.refresh(employee)

    return map_employee_to_schema(employee)


@router.get("/employees/", response_model=list[employee_schema.Employee])
def get_employees(
    skip: int = 0,
    limit: int = 10,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_admin_user)
):
    employees = db.query(model.Employee).offset(skip).limit(limit).all()
    return [map_employee_to_schema(employee) for employee in employees]


@router.get("/employees/{employee_id}", response_model=employee_schema.Employee)
def get_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_admin_user)
):
    employee = db.query(model.Employee).filter(model.Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    return map_employee_to_schema(employee)


@router.delete("/employees/{employee_id}")
def delete_employee(
    employee_id: int,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_admin_user)
):
    employee = db.query(model.Employee).filter(model.Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    db.delete(employee)
    db.commit()

    return JSONResponse(
		status_code=200,
		content={"message": "success"},
	)


@router.put("/employees/{employee_id}", response_model=employee_schema.Employee)
def update_employee(
    employee_id: int,
    payload: employee_schema.EmployeeUpdate,
    db: Session = Depends(get_db),
    current_user: UserBase = Depends(get_admin_user)
):
    employee = db.query(model.Employee).filter(model.Employee.id == employee_id).first()
    existing_user = db.query(model.User).filter(model.User.email == payload.email).first()
    if existing_user and existing_user.id != employee.user.id:
        raise HTTPException(status_code=400, detail="Email already registered")

    required_fields = ['first_name', 'last_name']
    for field in required_fields:
        if not getattr(payload, field):
            raise HTTPException(status_code=400, detail=f"{field.replace('_', ' ').title()} is required")

    for key, value in payload.dict().items():
        setattr(employee, key, value)

    db.commit()
    db.refresh(employee)
    return  map_employee_to_schema(employee)
