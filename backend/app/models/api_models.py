# Pydantic models go here
from pydantic import BaseModel
from typing import Optional, List, Dict


class ChatRequest(BaseModel):
    session_id: str
    message: str


class ChatResponse(BaseModel):
    response: str
    session_id: str
    metadata: Optional[Dict] = None
