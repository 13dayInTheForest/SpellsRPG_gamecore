from sqlalchemy import Table, Column, String, Integer, ForeignKey
from src.infrastructure.python_databases.database import metadata


kingdoms = Table(
    'kingdoms',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('group_id', String),
    Column('name', String),
    Column('title', String),  # Слоган королевства
    Column('avatar_url', String),
    Column('gold', Integer, default=0),
    Column('taxes', Integer, default=0),  # Сколько золота должны платить граждане каждый день

    Column('registered_by_user_id', Integer, ForeignKey('users.id', ondelete='SET NULL')),
)
