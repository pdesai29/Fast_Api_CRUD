from typing import List, Optional
from pydantic import BaseModel


class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool
