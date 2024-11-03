from sqlalchemy import Table, Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.sql import func
from src.db.python_databases.database import metadata

users = Table(
    'places',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('kingdom_id', Integer, ForeignKey('kingdoms.id', ondelete='CASCADE'), nullable=True, default=None),
    Column('name', String),
    Column('title', String),
    Column('avatar_url', String),

    Column('citizens_count', String),
    Column('date_created', DateTime, server_default=func.now()),
)
