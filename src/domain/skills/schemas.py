from pydantic import BaseModel
from typing import Optional


class SkillsSchema(BaseModel):
    id: str
    name: str
    dev_name: str
    description: str
    active: bool


class CreateSkillsSchema(BaseModel):
    name: str
    dev_name: str
    description: str
    active: bool = False


class UpdateSkillsSchema(BaseModel):
    name: str = None
    dev_name: str = None
    description: str = None
    active: bool = None


class SkillsQueryFilters(BaseModel):
    name: Optional[str] = None
    dev_name: Optional[str] = None
    description: Optional[str] = None
    active: Optional[bool] = None

