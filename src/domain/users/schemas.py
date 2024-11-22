from pydantic import BaseModel
import datetime
from typing import Optional


class UserSchema(BaseModel):
    id: int
    telegram_id: int
    first_name: str
    last_name: str
    username: str
    is_premium: bool
    can_join_groups: bool
    bio: str
    birthdate: datetime.date
    language_code: str
    current_character_id: Optional[int]
    souls_balance: int
    premium_player: bool
    characters_count: int
    death_count: int
    suicide_count: int
    can_play: bool
    can_create_characters: bool
    can_create_pictures: bool
    bot_blocked: bool
    start_play: datetime.datetime


class CreateUserSchema(BaseModel):
    telegram_id: int
    first_name: str
    last_name: str
    username: str
    is_premium: bool
    can_join_groups: bool
    bio: str
    birthdate: datetime.date
    language_code: str


class CreateUserSchemaForDB(CreateUserSchema):
    current_character_id: Optional[int] = None
    souls_balance: int = 0
    premium_player: bool = False
    characters_count: int = 0
    death_count: int = 0
    suicide_count: int = 0
    can_play: bool = True
    can_create_characters: bool = True
    can_create_pictures: bool = True
    bot_blocked: bool = False


class UpdateUserSchema(BaseModel):
    telegram_id: int = None
    first_name: str = None
    last_name: str = None
    username: str = None
    is_premium: bool = None
    can_join_groups: bool = None
    bio: str = None
    birthdate: datetime.date
    language_code: str = None
    current_character_id: int = None
    souls_balance: int = None
    premium_player: bool = None
    characters_count: int = None
    death_count: int = None
    suicide_count: int = None
    can_play: bool = None
    can_create_characters: bool = None
    can_create_pictures: bool = None
    bot_blocked: bool = None
