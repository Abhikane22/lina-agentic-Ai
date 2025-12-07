from pydantic import BaseModel
from typing import Optional, List


class UnderwritingRequest(BaseModel):
    customer_id: str
    amount: int
    tenure_months: int
    income: int
    existing_emi: int
    credit_score: int


class UnderwritingResponse(BaseModel):
    status: str                   # "APPROVED" | "CONDITIONAL" | "REJECTED"
    max_amount: Optional[int]
    interest_rate: Optional[float]
    reason: Optional[str] = None
    conditions: Optional[List[str]] = []
