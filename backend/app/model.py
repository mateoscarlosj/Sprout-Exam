from sqlalchemy import (ARRAY, Boolean, Column, Date, Enum, ForeignKey,
                        Integer, String)
from sqlalchemy.orm import relationship

from app.database import Base, SessionLocal
from app.enum import EmployeeType, UserType

from passlib.context import CryptContext

# User
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    user_type = Column(Enum(UserType), index=True)


def create_admin_user():
    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
    db = SessionLocal()
    hashed_password = pwd_context.hash("admin")
    if not db.query(User).filter(User.username == "admin").first():
        admin_user = User(username="admin", password=hashed_password, user_type="admin")
        db.add(admin_user)
        db.commit()
    db.close()

# Employee
class Employee(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    employee_type = Column(Enum(EmployeeType), index=True)

    number_of_leaves = Column(Integer, default=0)
    benefits = Column(ARRAY(String), nullable=True)

    contract_end_date = Column(Date)
    project = Column(String)
    is_active = Column(Boolean, default=True)

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="employees")

User.employees = relationship("Employee", back_populates="user", cascade="all, delete-orphan")