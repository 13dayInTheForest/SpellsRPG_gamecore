from sqlalchemy import Table, Column, String, Integer, Boolean
from src.db.database import metadata
from src.core.config import settings


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('hp', Integer),
    Column('age', Integer),
    Column('max_age', Integer),
    Column('gold', Integer),
    Column('min_atk', Integer),
    Column('max_atk', Integer),
    Column('exp_points', Integer),
    Column('title', Integer),

    Column('class_id', Integer),  # Должен быть привязан к таблице классов
    Column('potential_id', Integer),
    Column('god_id', Integer),
    Column('weakness_id', Integer),
    Column('born_kingdom_id', Integer),
    Column('current_location_id', Integer),
    Column('citizen_kingdom_id', Integer),

    Column('magic_lvl', Integer, default=5),
    Column('physical_lvl', Integer, default=5),
    Column('agility_lvl', Integer, default=5),
    Column('carma_lvl', Integer, default=5),

    Column('avatar_prompt', String, default=settings.DEFAULT_STYLE_PROMPT),
    Column('avatar_url', String),
    Column('avatar_can_change', Boolean, default=False),

    Column('dungeon_cleared', Integer),
    Column('monsters_killed', Integer),
    Column('human_killed', Integer),
    Column('friends_count', Integer),
)
