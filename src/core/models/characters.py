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
    Column('karma', Integer),
    Column('strength', Integer),
    Column('mana', Integer),
    Column('exp_points', Integer),
    Column('title', Integer),
    Column('type', String, default='player'),

    Column('can_speak', Boolean, default=True),
    Column('can_move', Boolean, default=True),
    Column('can_kill_players', Boolean, default=True),

    Column('user_id', Integer),
    Column('class_id', Integer),
    Column('potential_id', Integer),
    Column('god_id', Integer, default=1),  # Нужен дефолтный
    Column('weakness_id', Integer, default=None),
    Column('born_kingdom_id', Integer),
    Column('current_location_id', Integer),
    Column('citizen_kingdom_id', Integer),

    Column('avatar_prompt', String, default=settings.DEFAULT_STYLE_PROMPT),
    Column('avatar_url', String),

    Column('dungeon_cleared', Integer),
    Column('monsters_killed', Integer),
    Column('human_killed', Integer),
    Column('friends_count', Integer),
)
