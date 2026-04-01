# 🚀 HR Attendance Management System

A backend application built using **FastAPI** to manage employee attendance, leave requests, and reports.

---

## 📌 Features

- 👤 Employee Registration & Login
- ⏱ Attendance Management (Check-in / Check-out)
- 📝 Leave Management
  - Request Leave
  - Approve / Reject Leave
- 📊 Monthly Attendance Reports
- ✅ Input Validation & Error Handling
- 🧪 API Testing using Postman
- 🧪 Unit Testing using Pytest
- 🐳 Docker Support

---

## 🛠 Tech Stack

- FastAPI
- Python
- SQLite
- SQLAlchemy
- Pydantic
- Pytest
- Docker

---

## 📂 Project Structure
hr_attendance_system/
│
├── app/
│ ├── main.py
│ ├── database.py
│ ├── models.py
│ ├── schemas.py
│ ├── validators.py
│ ├── crud.py
│ └── routes/
│ ├── auth.py
│ ├── attendance.py
│ ├── leave.py
│ └── reports.py
│
├── test_api.py
├── requirements.txt
├── Dockerfile
└── README.md

---

## 🚀 How to Run

###  1. Clone the project

git clone <your-repo-link>
cd hr_attendance_system

### 2. Create a Virtual Environment
python -m venv virtual
.\virtual\Scripts\Activate

### 3. Install Dependencies
pip install -r requirements.txt

### 4. Run server
uvicorn app.main:app --reload 
### 5. Open Swagger
http://127.0.0.1:8000/docs

