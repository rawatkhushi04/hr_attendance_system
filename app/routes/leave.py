from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.models import LeaveRequest

router = APIRouter(prefix="/leave", tags=["Leave"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/request")
def request_leave(employee_id: int, reason: str, db: Session = Depends(get_db)):
    leave = LeaveRequest(
        employee_id=employee_id,
        reason=reason,
        status="pending"
    )
    db.add(leave)
    db.commit()
    db.refresh(leave)

    return {"message": "Leave requested", "leave_id": leave.id}


@router.put("/{id}/approve")
def approve_leave(id: int, db: Session = Depends(get_db)):

    leave = db.query(LeaveRequest).filter(LeaveRequest.id == id).first()

    if not leave:
        raise HTTPException(status_code=404, detail="Leave request not found")

    leave.status = "approved"

    db.commit()
    db.refresh(leave)

    return {
        "message": "Leave approved",
        "leave_id": id
    }


@router.put("/{id}/reject")
def reject_leave(id: int, db: Session = Depends(get_db)):

    leave = db.query(LeaveRequest).filter(LeaveRequest.id == id).first()

    if not leave:
        raise HTTPException(status_code=404, detail="Leave request not found")

    leave.status = "rejected"

    db.commit()
    db.refresh(leave)

    return {
        "message": "Leave rejected",
        "leave_id": id
    }


@router.get("/history/{employee_id}")
def history(employee_id: int, db: Session = Depends(get_db)):
    return db.query(LeaveRequest).filter(
        LeaveRequest.employee_id == employee_id
    ).all()