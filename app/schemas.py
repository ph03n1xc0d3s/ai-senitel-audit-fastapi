from pydantic import BaseModel, Field, EmailStr 
from typing import Optional

class AuditRequest(BaseModel):
    filename: str = Field(..., example="auth_service.py")
    content: str = Field(..., min_length=10, description="Source code to audit")
    language: str = "python"
    notified_email: EmailStr 

class AuditResponse(BaseModel):
    status: str 
    vulnerability_score: float: Field(ge=0, le=10)
    findings: list[str]