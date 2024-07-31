from enum import Enum


class EmployeeType(str, Enum):
    REGULAR = "regular"
    CONTRACTUAL = "contractual"


class UserType(str, Enum):
    ADMIN = "admin"
    EMPLOYEE = "employee"