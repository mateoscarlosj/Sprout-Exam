from app.schemas import employee as employee_schema

def map_employee_to_schema(employee):
    
    print(employee)
    return employee_schema.Employee(
        id=employee.id,
        first_name=employee.first_name,
        last_name=employee.last_name,
        employee_type=employee.employee_type,
        number_of_leaves=employee.number_of_leaves,
        benefits=employee.benefits,
        contract_end_date=employee.contract_end_date,
        project=employee.project,
        is_active=employee.is_active,
        email=employee.user.email
    )