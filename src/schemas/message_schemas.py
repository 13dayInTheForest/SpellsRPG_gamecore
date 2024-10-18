from pydantic import BaseModel
from typing import Any


class MessageSchema(BaseModel):
    message: str
    content: Any

