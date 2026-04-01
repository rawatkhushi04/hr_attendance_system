from fastapi import FastAPI
from app.database import engine, Base

from app.routes import auth, attendance, leave, reports

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(attendance.router)
app.include_router(leave.router)
app.include_router(reports.router)

@app.get("/")
def home():
    return {"message": "HR Management API Running"}