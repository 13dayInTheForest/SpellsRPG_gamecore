from sqlalchemy import Table, Column, String, Integer, Boolean
from src.db.python_databases.database import metadata


monsters = Table(
    'mobs_templates',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('mob_type', String),
    Column('hp_min', Integer),
    Column('hp_max', Integer),
    Column('age_min', Integer, default=1),
    Column('age_max', Integer, default=20),
    Column('gold_drop_min', Integer),
    Column('gold_drop_max', Integer),
    Column('karma_min', Integer),
    Column('karma_max', Integer),
    Column('strength_min', Integer),
    Column('strength_max', Integer),
    Column('mana_min', Integer),
    Column('mana_max', Integer),
    Column('exp_drop_min', Integer),
    Column('exp_drop_max', Integer),
    Column('can_drop_item', Boolean, default=False),
    Column('item_drop_chance_min', Integer, default=None),
    Column('item_drop_chance_max', Integer, default=None),
)
