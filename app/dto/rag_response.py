from pydantic import BaseModel
from typing import List

class RAGResponse(BaseModel):
    markdown_text: str
    followup_questions: List[str]
