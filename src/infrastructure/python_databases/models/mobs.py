from sqlalchemy import Table, Column, String, Integer, Boolean, ForeignKey, Enum
from src.infrastructure.python_databases.database import metadata
from src.domain.mobs import MobTypes


monsters = Table(
    'mobs',
    metadata,
    Column('name', String),
    Column('mob_type', String),
    Column('hp', Integer),
    Column('age', Integer, default=1),
    Column('gold', Integer),
    Column('karma', Integer),
    Column('strength', Integer),
    Column('mana', Integer),
    Column('title', Integer),
    Column('type', String, Enum(MobTypes).values_callable, default=MobTypes.Monster),

    Column('can_speak', Boolean, default=True),
    Column('can_move', Boolean, default=True),
    Column('can_defend', Boolean, default=True),
    Column('can_have_friends', Boolean, default=False),
    Column('can_be_revived', Boolean, default=False),
    Column('can_kill_players', Boolean, default=True),

    Column('controlled_by', Integer, ForeignKey('characters.id', ondelete='CASCADE'), default=None),

    Column('avatar_url', String),

    Column('class_id', Integer),
    Column('potential_id', Integer, default=None),
    Column('god_id', Integer, default=None),
    Column('weakness_id', Integer, default=None),
    Column('born_kingdom_id', Integer, default=None),
    Column('current_location_id', Integer, default=None),
    Column('citizen_kingdom_id', Integer, default=None),
)
