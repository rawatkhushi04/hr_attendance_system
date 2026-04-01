from sqlalchemy.orm import Session
from app.models import Employee

def create_user(db: Session, user):
    db_user = Employee(**user.dict())
    db.add(db_user)
    db.commit()
    return db_user