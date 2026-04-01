from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from datetime import datetime, date

from app.database import SessionLocal
from app.models import Attendance

router = APIRouter(prefix="/attendance")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/checkin")
def checkin(employee_id: int, db: Session = Depends(get_db)):
    record = Attendance(
        employee_id=employee_id,
        check_in=datetime.now(),
        date=date.today()
    )
    db.add(record)
    db.commit()
    return {"message": "Checked in"}

@router.post("/checkout")
def checkout(employee_id: int, db: Session = Depends(get_db)):
    today = date.today()

    record = db.query(Attendance).filter(
        Attendance.employee_id == employee_id,
        Attendance.date == today
    ).first()

    if not record:
        return {"error": "No check-in found"}

    record.check_out = datetime.now()
    db.commit()

    return {"message": "Checked out"}

@router.get("/{employee_id}")
def history(employee_id: int, db: Session = Depends(get_db)):
    return db.query(Attendance).filter(
        Attendance.employee_id == employee_id
    ).all()