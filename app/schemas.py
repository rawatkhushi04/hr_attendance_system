from pydantic import BaseModel

class EmployeeCreate(BaseModel):
    name: str
    email: str
    password: str

class LoginSchema(BaseModel):
    email: str
    password: str

class LeaveSchema(BaseModel):
    employee_id: int
    reason: str