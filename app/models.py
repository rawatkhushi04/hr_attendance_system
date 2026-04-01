from sqlalchemy import Column, Integer, String, DateTime, Date
from app.database import Base

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Attendance(Base):
    __tablename__ = "attendance"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    check_in = Column(DateTime)
    check_out = Column(DateTime)
    date = Column(Date)

class LeaveRequest(Base):
    __tablename__ = "leave_requests"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    reason = Column(String)
    status = Column(String, default="pending")
    start_date = Column(Date)
    end_date = Column(Date)

class LeaveBalance(Base):
    __tablename__ = "leave_balances"
    id = Column(Integer, primary_key=True)
    employee_id = Column(Integer)
    total_leaves = Column(Integer, default=10)