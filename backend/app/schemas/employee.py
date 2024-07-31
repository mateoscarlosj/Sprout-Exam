from datetime import date
from typing import List, Optional

from pydantic import BaseModel, EmailStr

from app.enum import EmployeeType


class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    employee_type: EmployeeType

    class Config:
        orm_mode = True


class EmployeeCreate(EmployeeBase):
    email: EmailStr
    username: Optional[str] = None
    number_of_leaves: Optional[int] = None
    benefits: Optional[List[str]] = None
    contract_end_date: Optional[date] = None
    project: Optional[str] = None

class EmployeeUpdate(EmployeeBase):
    email: EmailStr
    number_of_leaves: Optional[int] = None
    benefits: Optional[List[str]] = None
    contract_end_date: Optional[date] = None
    project: Optional[str] = None


class Employee(EmployeeBase):
    id: int
    number_of_leaves: Optional[int] = None
    benefits: Optional[List[str]] = None
    contract_end_date: Optional[date] = None
    project: Optional[str] = None
    is_active: Optional[bool] = True
    email:str


    class Config:
        orm_mode = True
