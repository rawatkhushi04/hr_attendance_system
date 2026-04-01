from fastapi import HTTPException

def validate_email(email: str):
    if not email.endswith("@navikenz.com"):
        raise HTTPException(
            status_code=400,
            detail="Only @navikenz.com emails allowed"
        )

def validate_positive(value: int):
    if value <= 0:
        raise HTTPException(
            status_code=400,
            detail="Value must be positive"
        )