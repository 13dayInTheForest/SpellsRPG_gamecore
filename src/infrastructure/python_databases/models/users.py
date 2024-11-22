from sqlalchemy import Table, Column, String, Integer, Boolean, DateTime
from sqlalchemy.sql import func
from src.infrastructure.python_databases.database import metadata


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('telegram_id', String),
    Column('first_name', String),
    Column('last_name', String),
    Column('username', String),
    Column('is_premium', Boolean),
    Column('can_join_groups', Boolean),
    Column('bio', String),
    Column('birthdate', DateTime),
    Column('language_code', String),

    Column('current_character_id', Integer, default=None, nullable=True),
    Column('souls_balance', Integer, default=0),
    Column('premium_player', Boolean, default=False),

    Column('characters_count', Integer, default=0),
    Column('death_count', Integer, default=0),
    Column('suicide_count', Integer, default=0),

    Column('can_play', Boolean, default=True),
    Column('can_create_characters', Boolean, default=True),
    Column('can_create_pictures', Boolean, default=True),

    Column('bot_blocked', Boolean, default=False),
    Column('start_play', DateTime, server_default=func.now())
)
