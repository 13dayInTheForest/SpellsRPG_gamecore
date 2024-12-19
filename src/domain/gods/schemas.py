from pydantic import BaseModel
from typing import Optional


class CreateGodSchema(BaseModel):
    active: bool = False
    name: str
    description: str
    terms: str
    picture_url: str
    needs_count: int
    needs: list = []
    changes: list = []
    fight_changes: list = []
    to_stop: list = []
    abilities: list = []


class GodsSchema(BaseModel):
    id: str
    active: bool
    name: str
    description: str
    terms: str
    picture_url: str
    needs: list
    needs_count: int
    changes: list
    fight_changes: list
    to_stop: list
    abilities: list


class UpdateGodsSchema(BaseModel):
    name: str = None
    active: bool = None
    description: str = None
    terms: str = None
    picture_url: str = None
    needs_count: int = None
    needs: list = None
    changes: list = None
    fight_changes: list = None
    to_stop: list = None
    abilities: list = None


class GodsQueryFilters(BaseModel):
    name: Optional[str] = None
    active: Optional[bool] = None
    description: Optional[str] = None
    terms: Optional[str] = None
    picture_url: Optional[str] = None
    needs_count: Optional[int] = None


