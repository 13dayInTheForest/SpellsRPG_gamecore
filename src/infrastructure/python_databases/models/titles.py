from sqlalchemy import Table, Column, Integer, String
from src.infrastructure.python_databases.database import metadata


titles = Table(
    'titles',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String)
)

