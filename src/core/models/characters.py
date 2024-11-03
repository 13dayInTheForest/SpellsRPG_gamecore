from sqlalchemy import Table, Column, String, Integer, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from src.db.python_databases.database import metadata
from src.core.config import settings


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100)),
    Column('hp', Integer, default=100),
    Column('age', Integer, default=18),
    Column('max_age', Integer),
    Column('gold', Integer, default=100),
    Column('karma', Integer, default=10),
    Column('strength', Integer, default=10),
    Column('mana', Integer, default=10),
    Column('exp_points', Integer, default=0),
    Column('title', Integer, default=None),
    Column('type', String, default='player'),
    Column('born_date', DateTime, server_default=func.now()),

    Column('can_speak', Boolean, default=True),
    Column('can_move', Boolean, default=True),
    Column('can_play', Boolean, default=True),
    Column('can_fight', Boolean, default=True),
    Column('can_defend', Boolean, default=True),
    Column('can_have_friends', Boolean, default=True),
    Column('can_be_revived', Boolean, default=False),
    Column('can_kill_players', Boolean, default=True),

    Column('user_id', Integer, ForeignKey('users.id', ondelete='SET NULL')),
    Column('class_id', Integer, ForeignKey('classes.id', ondelete='SET NULL')),
    Column('potential_id', Integer, ForeignKey('potentials.id', ondelete='SET NULL')),
    Column('god_id', Integer, ForeignKey('gods.id', ondelete='SET NULL')),
    Column('weakness_id', Integer, ForeignKey('weaknesses.id', ondelete='SET NULL')),
    Column('born_kingdom_id', Integer, ForeignKey('kingdoms.id', ondelete='SET NULL')),
    Column('citizen_kingdom_id', Integer, ForeignKey('kingdoms.id', ondelete='SET NULL')),

    Column('avatar_prompt', String, default=settings.DEFAULT_STYLE_PROMPT),
    Column('avatar_url', String),

    Column('dungeon_cleared', Integer, default=0),
    Column('monsters_killed', Integer, default=0),
    Column('human_killed', Integer, default=0),
    Column('friends_count', Integer, default=0)
)
