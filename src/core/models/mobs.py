from sqlalchemy import Table, Column, String, Integer, Boolean, ForeignKey, Enum
from src.db.python_databases.database import metadata
from src.mobs.schemas import MobTypes


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
    Column('exp_points_for_kill', Integer),
    Column('title', Integer),
    Column('type', String, Enum(MobTypes, )),  # ДОДЕЛАТЬ
    Column('peaceful', String, default='monster'),

    Column('mercy_chance', Integer, default=100_000),
    Column('min_self_hp_to_run', Integer, default=1),
    Column('min_self_hp_to_run', Integer, default=1),

    Column('item_drop', Integer, default=None),  # FK
    Column('item_drop_chance', Integer, default=100),  # 1 к 100

    Column('can_speak', Boolean, default=True),
    Column('can_move', Boolean, default=True),
    Column('can_defend', Boolean, default=True),
    Column('can_have_friends', Boolean, default=False),
    Column('can_be_revived', Boolean, default=False),
    Column('can_kill_players', Boolean, default=True),

    Column('can_be_controlled', Boolean, default=True),
    Column('controlled_by', Integer, ForeignKey('characters.id', ondelete='SET NULL'), default=None),

    Column('avatar_url', String),

    Column('class_id', Integer),
    Column('potential_id', Integer, default=None),
    Column('god_id', Integer, default=None),
    Column('weakness_id', Integer, default=None),
    Column('born_kingdom_id', Integer, default=None),
    Column('current_location_id', Integer, default=None),
    Column('citizen_kingdom_id', Integer, default=None),

    Column('run_if_hp_le', Integer, default=0),
    Column('run_chance', Integer, default=0),
)
