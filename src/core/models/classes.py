from sqlalchemy import Table, Column, String, Integer, Boolean, JSON
from src.db.database import metadata


classes = Table(
    'classes',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('description', String),
    Column('terms', String),
    Column('picture_url', String),

    # Все значения взяты с таблицы users.
    Column('needs', JSON, default='{}'),  # Что нужно от игрока для класса
    Column('changes', JSON, default='{}'),  # Баффы и Нерфы для игрока
    Column('fight_changes', JSON, default='{}')  # Баффы и Нерфы для игрока во время боя
    # пример условий во время боя:
    # {поле врага: {значение поля:{поле игрока: значение которое нужно прибавить}}}
    # {}
)