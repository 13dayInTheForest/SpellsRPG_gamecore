from pydantic import BaseModel
from typing import Optional


class ClassesSchema(BaseModel):
    id: int
    name: str
    description: str
    terms: Optional[str]
    picture_url: Optional[str]
    needs: list
    changes: list
    skills: list


class CreateClassesSchema(BaseModel):
    name: str
    description: str
    terms: str
    picture_url: str = None
    needs: list = []
    changes: list
    skills: list


class UpdateClassesSchema(BaseModel):
    name: str = None
    description: str = None
    terms: str = None
    picture_url: str = None
    needs: list = None
    changes: list = None
    skills: list = None


class ClassQueryFilters(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    terms: Optional[str] = None
    picture_url: Optional[str] = None
    needs: Optional[list] = None
    changes: Optional[list] = None
    skills: Optional[list] = None
