from databases import Database
from sqlalchemy import MetaData
from sqlalchemy.dialects import postgresql
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.schema import CreateTable, DropTable

from src.core.config import settings


database = Database(settings.get_db_url)
async_engine = create_async_engine(settings.get_db_url)
metadata = MetaData()
dialect = postgresql.dialect()


async def get_db():
    return database


async def create_tables():
    for table in metadata.tables.values():
        query = str(CreateTable(table, if_not_exists=True).compile(dialect=dialect))
        await database.execute(query=query)


async def delete_tables():
    for table in metadata.tables.values():
        query = str(DropTable(table).compile(dialect=dialect))
        await database.execute(query=query)
