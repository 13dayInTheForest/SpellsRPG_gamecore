from pydantic import BaseModel, Field
from typing import Optional, Literal
from datetime import datetime
from src.infrastructure.config import settings


class CharacterSchema(BaseModel):
    id: int
    name: str
    hp: int
    max_age: int
    max_mana: int
    max_hp: int
    gold: int
    karma: int
    strength: int
    mana: int
    shield: int
    max_shield: int
    exp_points: int
    title: Optional[str]
    type: str
    reputation: Optional[int]
    born_date: datetime
    unlimited_mana: bool
    unlimited_karma: bool
    unlimited_strength: bool
    unlimited_shield: bool
    armor: Optional[str]
    weapon: Optional[str]
    backpack_size: int
    can_speak: bool
    can_hear: bool
    can_see: bool
    can_move: bool
    can_play: bool
    can_fight: bool
    can_defend: bool
    can_worship_gods: bool
    can_have_items: bool
    can_have_backpack: bool
    can_have_friends: bool
    can_kill_players: bool
    can_be_killed: bool
    can_be_seen: bool
    can_be_revived: bool
    can_be_cursed: bool
    can_be_healed: bool
    telegram_user_id: Optional[str]
    class_id: Optional[str]
    potential_id: Optional[str]
    god_id: Optional[str]
    weakness_id: Optional[str]
    born_kingdom_id: Optional[int]
    citizen_kingdom_id: Optional[int]
    avatar_prompt: str
    avatar_prompt_ru: str
    avatar_url: str
    dungeon_cleared: int
    monsters_killed: int
    human_killed: int
    friends_count: int
    short_texts: bool


class CreateCharacterSchema(BaseModel):
    telegram_user_id: Optional[str]
    name: str = Field(..., min_length=2, max_length=100)


class CreateCharacterSchemaForDB(CreateCharacterSchema):
    avatar_prompt: str = ''
    avatar_prompt_ru: str = ''
    avatar_url: str = ''
    hp: int = 100
    max_age: int = 70
    max_mana: int = 10
    max_hp: int = 100
    max_strength: int = 10
    max_karma: int = 10
    gold: int = 100
    karma: int = 10
    strength: int = 10
    mana: int = 10
    shield: int = 0
    max_shield: int = 0
    exp_points: int = 10
    title: Optional[str] = None
    type: str = 'player'
    reputation: int = 0
    unlimited_mana: bool = False
    unlimited_karma: bool = False
    unlimited_strength: bool = False
    unlimited_shield: bool = False
    armor: Optional[str] = None
    weapon: Optional[str] = None
    backpack_size: int = 10
    can_speak: bool = True
    can_hear: bool = True
    can_see: bool = True
    can_move: bool = True
    can_play: bool = True
    can_fight: bool = True
    can_defend: bool = True
    can_worship_gods: bool = True
    can_have_items: bool = True
    can_have_backpack: bool = True
    can_have_friends: bool = True
    can_kill_players: bool = True
    can_be_killed: bool = True
    can_be_seen: bool = True
    can_be_revived: bool = False
    can_be_cursed: bool = True
    can_be_healed: bool = True
    telegram_user_id: Optional[str] = None
    class_id: Optional[str] = None
    potential_id: Optional[str] = None
    god_id: Optional[str] = None
    weakness_id: Optional[str] = None
    born_kingdom_id: Optional[int] = None
    citizen_kingdom_id: Optional[int] = None
    dungeon_cleared: int = 0
    monsters_killed: int = 0
    human_killed: int = 0
    friends_count: int = 0
    short_texts: bool = False


class UpdateCharacterSchema(BaseModel):
    name: str = None
    hp: int = None
    max_age: int = None
    max_mana: int = None
    max_hp: int = None
    gold: int = None
    karma: int = None
    strength: int = None
    mana: int = None
    shield: int = None
    max_shield: int = None
    exp_points: int = None
    title: Optional[str] = None
    type: str = None
    reputation: int = None
    unlimited_mana: bool = None
    unlimited_karma: bool = None
    unlimited_strength: bool = None
    unlimited_shield: bool = None
    armor: Optional[str] = None
    weapon: Optional[str] = None
    backpack_size: int = None
    can_speak: bool = None
    can_hear: bool = None
    can_see: bool = None
    can_move: bool = None
    can_play: bool = None
    can_fight: bool = None
    can_defend: bool = None
    can_worship_gods: bool = True
    can_have_items: bool = True
    can_have_backpack: bool = True
    can_have_friends: bool = None
    can_kill_players: bool = None
    can_be_killed: bool = None
    can_be_seen: bool = None
    can_be_revived: bool = None
    can_be_cursed: bool = None
    can_be_healed: bool = None
    telegram_user_id: Optional[str] = None
    class_id: Optional[str] = None
    potential_id: Optional[str] = None
    god_id: Optional[str] = None
    weakness_id: Optional[str] = None
    born_kingdom_id: Optional[int] = None
    citizen_kingdom_id: Optional[int] = None
    avatar_prompt: str = None
    avatar_prompt_ru: str = None
    avatar_url: str = None
    dungeon_cleared: int = None
    monsters_killed: int = None
    human_killed: int = None
    friends_count: int = None
    short_texts: bool = None


class CharacterQueryFilters(BaseModel):
    id: Optional[int] = None
    name: Optional[str] = None
    hp: Optional[int] = None
    max_age: Optional[int] = None
    max_mana: Optional[int] = None
    max_hp: Optional[int] = None
    gold: Optional[int] = None
    karma: Optional[int] = None
    strength: Optional[int] = None
    mana: Optional[int] = None
    shield: Optional[int] = None
    max_shield: Optional[int] = None
    exp_points: Optional[int] = None
    title: Optional[str] = None
    type: Optional[str] = None
    reputation: Optional[int] = None
    born_date: Optional[datetime] = None
    unlimited_mana: Optional[bool] = None
    unlimited_karma: Optional[bool] = None
    unlimited_strength: Optional[bool] = None
    unlimited_shield: Optional[bool] = None
    armor: Optional[str] = None
    weapon: Optional[str] = None
    backpack_size: Optional[int] = None
    can_speak: Optional[bool] = None
    can_hear: Optional[bool] = None
    can_see: Optional[bool] = None
    can_move: Optional[bool] = None
    can_play: Optional[bool] = None
    can_fight: Optional[bool] = None
    can_defend: Optional[bool] = None
    can_worship_gods: Optional[bool] = None
    can_have_items: Optional[bool] = None
    can_have_backpack: Optional[bool] = None
    can_have_friends: Optional[bool] = None
    can_kill_players: Optional[bool] = None
    can_be_killed: Optional[bool] = None
    can_be_seen: Optional[bool] = None
    can_be_revived: Optional[bool] = None
    can_be_cursed: Optional[bool] = None
    can_be_healed: Optional[bool] = None
    telegram_user_id: Optional[str] = None
    class_id: Optional[str] = None
    potential_id: Optional[str] = None
    god_id: Optional[str] = None
    weakness_id: Optional[str] = None
    born_kingdom_id: Optional[int] = None
    citizen_kingdom_id: Optional[int] = None
    avatar_prompt: Optional[str] = None
    avatar_prompt_ru: Optional[str] = None
    avatar_url: Optional[str] = None
    dungeon_cleared: Optional[int] = None
    monsters_killed: Optional[int] = None
    human_killed: Optional[int] = None
    friends_count: Optional[int] = None
    short_texts: Optional[bool] = None


class CharacterBattleSchema(BaseModel):
    """skills: ['DEV_name', 'DEV_name']"""
    skills: list
    class_dev_name: str

    id: int
    name: str
    hp: int
    max_age: int
    max_mana: int
    max_hp: int
    gold: int
    karma: int
    strength: int
    mana: int
    shield: int
    max_shield: int
    exp_points: int
    title: Optional[str]
    type: str
    reputation: Optional[int]
    born_date: datetime
    unlimited_mana: bool
    unlimited_karma: bool
    unlimited_strength: bool
    unlimited_shield: bool
    armor: Optional[str]
    weapon: Optional[str]
    backpack_size: int
    can_speak: bool
    can_hear: bool
    can_see: bool
    can_move: bool
    can_play: bool
    can_fight: bool
    can_defend: bool
    can_worship_gods: bool
    can_have_items: bool
    can_have_backpack: bool
    can_have_friends: bool
    can_kill_players: bool
    can_be_killed: bool
    can_be_seen: bool
    can_be_revived: bool
    can_be_cursed: bool
    can_be_healed: bool
    telegram_user_id: Optional[str]
    class_id: Optional[str]
    potential_id: Optional[str]
    god_id: Optional[str]
    weakness_id: Optional[str]
    born_kingdom_id: Optional[int]
    citizen_kingdom_id: Optional[int]
    avatar_prompt: str
    avatar_prompt_ru: str
    avatar_url: str
    dungeon_cleared: int
    monsters_killed: int
    human_killed: int
    friends_count: int
    short_texts: bool
