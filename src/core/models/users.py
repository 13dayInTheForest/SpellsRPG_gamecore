from sqlalchemy import Table, Column, String, Integer, Boolean, Float, DateTime
from sqlalchemy.sql import func
from src.db.python_databases.database import metadata


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('first_name', String),
    Column('last_name', String),
    Column('username', String),
    Column('is_premium', String),
    Column('can_join_groups', String),
    Column('bio', String),
    Column('birthdate', String),
    Column('language_code', String),

    Column('current_character_id', Integer, default=None),
    Column('balance', Float, default=0.0),
    Column('premium_player', Boolean, default=False),

    Column('death_count', Integer, default=0),

    Column('can_play', Boolean, default=True),
    Column('can_create_characters', Boolean, default=True),
    Column('can_create_pictures', Boolean, default=True),

    Column('bot_blocked', Boolean, default=False),
    Column('start_play', DateTime, server_default=func.now())
)
