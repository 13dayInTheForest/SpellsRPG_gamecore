from sqlalchemy import Table, Column, String, Integer, Boolean, JSON
from src.db.database import metadata


dungeons = Table(
    'dungeons',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('description', String),
    Column('price', Integer),
    Column('dangerous_lvl', Integer),
    Column('', ),
    Column('', ),
)
