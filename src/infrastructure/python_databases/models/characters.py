from sqlalchemy import Table, Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.infrastructure.python_databases.database import metadata
from src.infrastructure.config import settings


characters = Table(
    'characters',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('hp', Integer, default=100),
    Column('max_age', Integer, default=70),
    Column('gold', Integer, default=100),
    Column('karma', Integer, default=10),
    Column('strength', Integer, default=10),
    Column('mana', Integer, default=10),
    Column('exp_points', Integer, default=0),
    Column('title', String, ForeignKey('titles.id', ondelete='SET NULL'), default=None, nullable=True),
    Column('type', String, default='player'),
    Column('born_date', DateTime, server_default=func.now()),

    Column('armor', String, default=None, nullable=True),
    Column('weapon', String, default=None, nullable=True),
    Column('backpack_size', Integer, default=10),

    Column('can_speak', Boolean, default=True),
    Column('can_hear', Boolean, default=True),
    Column('can_see', Boolean, default=True),
    Column('can_move', Boolean, default=True),
    Column('can_play', Boolean, default=True),
    Column('can_fight', Boolean, default=True),
    Column('can_defend', Boolean, default=True),

    Column('can_worship_gods', Boolean, default=True),
    Column('can_have_items', Boolean, default=True),
    Column('can_have_backpack', Boolean, default=True),
    Column('can_have_friends', Boolean, default=True),
    Column('can_kill_players', Boolean, default=True),

    Column('can_be_killed', Boolean, default=True),
    Column('can_be_seen', Boolean, default=True),
    Column('can_be_revived', Boolean, default=True),
    Column('can_be_cursed', Boolean, default=True),
    Column('can_be_healed', Boolean, default=True),

    Column('class_id', String, default=None, nullable=True),  # Коллекция MongoDB
    Column('potential_id', String, default=None, nullable=True),  # ---^
    Column('god_id', String, default=None, nullable=True),  # ---------|
    Column('weakness_id', String, default=None, nullable=True),  # ----|
    Column('born_kingdom_id', Integer, ForeignKey('kingdoms.id', ondelete='SET NULL'), nullable=True),
    Column('citizen_kingdom_id', Integer, ForeignKey('kingdoms.id', ondelete='SET NULL'), nullable=True),

    Column('avatar_prompt', String, default=settings.DEFAULT_STYLE_PROMPT),
    Column('avatar_prompt_ru', String, default=settings.DEFAULT_STYLE_PROMPT),
    Column('avatar_url', String),

    Column('dungeon_cleared', Integer, default=0),
    Column('monsters_killed', Integer, default=0),
    Column('human_killed', Integer, default=0),
    Column('friends_count', Integer, default=0)
)
