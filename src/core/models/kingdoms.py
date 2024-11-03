from sqlalchemy import Table, Column, String, Integer
from src.db.python_databases.database import metadata


users = Table(
    'kingdoms',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('title', String),
    Column('avatar_url', String),
    Column('emblem_url', String),

    Column('citizens_count', String),
)
