from pydantic import BaseModel
from typing import Optional


class CreateKingdomSchema(BaseModel):
    group_id: str
    name: str
    title: Optional[str] = None
    avatar_url: Optional[str]
    gold: int
    taxes: int
    registered_by_user_id: Optional[int]


class KingdomSchema(BaseModel):
    id: int
    group_id: str
    name: str
    title: Optional[str]
    avatar_url: Optional[str]
    gold: int
    taxes: int
    registered_by_user_id: Optional[int]


class UpdateKingdomSchema(BaseModel):
    group_id: str = None
    name: str = None
    title: Optional[str] = None
    avatar_url: Optional[str] = None
    gold: int = None
    taxes: int = None
    registered_by_user_id: Optional[int] = None
