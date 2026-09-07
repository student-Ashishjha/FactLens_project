from pydantic import BaseModel
from datetime import datetime


class ClaimCreate(BaseModel):
    text: str


class ClaimResponse(BaseModel):
    id: int
    text: str
    status: str
    created_at: datetime

    class Config:
        from_attributes = True