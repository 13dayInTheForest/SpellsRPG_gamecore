from pydantic import BaseModel
from typing import Any, Dict, List, Optional
from fastapi import Query


class CreateGodSchema(BaseModel):
    active: bool = False
    name: str
    description: str
    terms: str
    picture_url: str
    needs: Dict[str, Any] = {}
    changes: List[str] = []
    fight_changes: List[str] = []
    abilities: List[str] = []


class GodsSchema(BaseModel):
    id: Optional[str]
    active: bool
    name: str
    description: str
    terms: str
    picture_url: str
    needs: Dict[str, Any]
    changes: List[str]
    fight_changes: List[str]
    abilities: List[str]


class UpdateGodsSchema(BaseModel):
    name: str = None
    active: bool = None
    description: str = None
    terms: str = None
    picture_url: str = None
    needs: Dict[str, Any] = None
    changes: List[str] = None
    fight_changes: List[str] = None
    abilities: List[str] = None


class GodsQueryFilters(BaseModel):
    name: Optional[str] = None
    active: Optional[bool] = None
    description: Optional[str] = None
    terms: Optional[str] = None
    picture_url: Optional[str] = None

