from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


# Test Home Route
def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "HR Management API Running"}


# Test Register API
import random

def test_register():
    email = f"test{random.randint(1,10000)}@navikenz.com"

    response = client.post("/auth/register", json={
        "name": "Test User",
        "email": email,
        "password": "123456"
    })

    assert response.status_code == 200


# Test Invalid Email (Validation)
def test_invalid_email():
    response = client.post("/auth/register", json={
        "name": "Test User",
        "email": "test@gmail.com",  # invalid domain
        "password": "123456"
    })
    assert response.status_code == 400


#  Test Attendance Check-in
def test_checkin():
    response = client.post("/attendance/checkin?employee_id=1")
    assert response.status_code in [200, 400]


def test_monthly_report():
    response = client.get("/reports/monthly/all", params={
        "month": 9,
        "year": 2026
    })
    assert response.status_code in [200, 404]