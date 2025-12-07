# Pydantic models go here
from pydantic import BaseModel
from typing import Optional


class CustomerProfile(BaseModel):
    customer_id: str
    kyc_status: str   # "VERIFIED" or "NOT_FOUND"
    income: Optional[int] = None
    existing_emi: Optional[int] = None
    preapproved_limit: Optional[int] = None
