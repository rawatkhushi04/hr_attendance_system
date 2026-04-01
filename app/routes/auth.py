from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import Employee
from app.schemas import EmployeeCreate, LoginSchema  

router = APIRouter(prefix="/auth")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/register")
def register(user: EmployeeCreate, db: Session = Depends(get_db)):
    validate_email(user.email)
    new_user = Employee(**user.model_dump())
    db.add(new_user)
    db.commit()
    return {"message": "User registered"}

@router.post("/login")
def login(user: LoginSchema, db: Session = Depends(get_db)):
    db_user = db.query(Employee).filter(Employee.email == user.email).first()

    if not db_user or db_user.password != user.password:
        return {"error": "Invalid credentials"}

    return {"message": "Login successful", "user_id": db_user.id}
from app.validators import validate_email

