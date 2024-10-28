from sqlalchemy import Table, Column, String, Integer, Boolean, JSON
from src.db.database import metadata


monsters = Table(
    'monsters',
    metadata,
    Column('id', Integer, primary_key=True),
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
    Column('type', String, default='monster'),
    Column('', ),
    Column('', ),
    Column('', ),
)