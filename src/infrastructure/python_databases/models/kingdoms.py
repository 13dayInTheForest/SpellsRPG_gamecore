from sqlalchemy import Table, Column, String, Integer, ForeignKey
from src.infrastructure.python_databases.database import metadata


users = Table(
    'kingdoms',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('group_id', Integer),
    Column('name', String),
    Column('title', String),  # Слоган королевства
    Column('avatar_url', String),
    Column('gold', Integer, default=0),
    Column('lvl', Integer, default=0),

    Column('citizens_count', Integer),
    Column('registered_by_user_id', Integer, ForeignKey('users.id', ondelete='SET NULL')),
    Column('king', Integer, ForeignKey('users.id', ondelete='SET NULL'))
)
