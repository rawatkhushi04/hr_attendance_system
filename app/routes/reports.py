from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import SessionLocal
from app.models import Attendance

router = APIRouter(prefix="/reports", tags=["Reports"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#  all employees
@router.get("/monthly/all")
def monthly_all_report(month: int, year: int, db: Session = Depends(get_db)):

    records = db.query(
        Attendance.employee_id,
        func.count(Attendance.id)
    ).filter(
        func.strftime("%m", Attendance.check_in) == f"{month:02}",
        func.strftime("%Y", Attendance.check_in) == str(year)
    ).group_by(Attendance.employee_id).all()

    return [
        {
            "employee_id": r[0],
            "total_days_present": r[1]
        }
        for r in records
    ]


#individual employee
@router.get("/monthly/{employee_id}")
def monthly_report(employee_id: int, month: int, year: int, db: Session = Depends(get_db)):

    records = db.query(Attendance).filter(
        Attendance.employee_id == employee_id,
        func.strftime("%m", Attendance.check_in) == f"{month:02}",
        func.strftime("%Y", Attendance.check_in) == str(year)
    ).all()

    return {
        "employee_id": employee_id,
        "total_days_present": len(records)
    }