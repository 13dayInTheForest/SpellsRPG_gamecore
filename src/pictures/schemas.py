from datetime import datetime
from typing import Annotated

from fastapi import UploadFile, File
from pydantic import BaseModel, constr
from src.core.config import settings


class CreatePicRequest(BaseModel):
    username: str
    prompt: constr(max_length=200) = settings.TEMPLE_PROFILE_PROMPT


class PicDetail(BaseModel):
    user: str
    prompt: str
    time_generated: datetime = datetime.utcnow()
    url: str
    response_time: float


