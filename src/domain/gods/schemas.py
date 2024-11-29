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
    changes: Dict[str, Any] = {}
    fight_changes: Dict[str, Any] = {}
    abilities: List[str] = []


class GodsSchema(BaseModel):
    id: Optional[str]
    active: bool
    name: str
    description: str
    terms: str
    picture_url: str
    needs: Dict[str, Any]
    changes: Dict[str, Any]
    fight_changes: Dict[str, Any]
    abilities: List[str]


class UpdateGodsSchema(BaseModel):
    name: str = None
    active: bool = None
    description: str = None
    terms: str = None
    picture_url: str = None
    needs: Dict[str, Any] = None
    changes: Dict[str, Any] = None
    fight_changes: Dict[str, Any] = None
    abilities: List[str] = None


class GodsQueryFilters(BaseModel):
    name: Optional[str] = None
    active: Optional[bool] = None
    description: Optional[str] = None
    terms: Optional[str] = None
    picture_url: Optional[str] = None

