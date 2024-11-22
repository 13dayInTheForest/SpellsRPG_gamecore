from sqlalchemy import Table, Column, String, Integer, ForeignKey
from src.infrastructure.python_databases.database import metadata


users = Table(
    'kingdoms',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('kingdom_id', Integer),
    Column('name', String),
    Column('title', String),
    Column('avatar_url', String),
    Column('emblem_url', String),

    Column('citizens_count', String),
    Column('registered_by_user_id', Integer, ForeignKey('users.id', ondelete='SET NULL')),
    Column('registered_by_user_id', Integer, ForeignKey('users.id', ondelete='SET NULL')),
)
