# Pydantic models go here
from pydantic import BaseModel
from typing import Optional, List


class LoanApplication(BaseModel):
    amount: Optional[int] = None
    tenure_months: Optional[int] = None
    purpose: Optional[str] = None
    income: Optional[int] = None
    existing_emi: Optional[int] = None
    credit_score: Optional[int] = None
    customer_id: Optional[str] = None
