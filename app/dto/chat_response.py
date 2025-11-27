from pydantic import BaseModel
from typing import List


class ChatResponse(BaseModel):
    answer: str
    session_id: str
    followups: List[str]