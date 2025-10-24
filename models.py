from pydantic import BaseModel, Field
from typing import List

class Ticket(BaseModel):
    channel: str
    severity: str
    summary: str

class ResponseModel(BaseModel):
    decision: str
    reasoning: str
    checklist: List[str] = Field(default_factory=list)
