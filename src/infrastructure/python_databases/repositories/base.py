from typing import Generic, TypeVar, Type
from pydantic import BaseModel
from sqlalchemy import Table
from databases import Database


class BaseRepo:
    def __init__(self, db: Database, model: Type[Table], schema: Type[BaseModel]):
        self.db = db
        self.model = model
        self.schema = schema  # Схема самой сущности по типу UserSchema

    async def create(self, obj: Type[BaseModel]) -> None:
        query = self.model.insert().values(**obj.dict())
        return await self.db.execute(query=query)

    async def read(self, obj_id: int) -> Type[BaseModel] | None:
        query = self.model.select().where(self.model.c.id == obj_id)
        response = await self.db.fetch_one(query=query)
        return self.schema(**dict(response)) if response else None

    async def update(self, obj_id: int, obj_updates: Type[BaseModel]) -> None:
        query = self.model.update().values(**obj_updates.dict(exclude_none=True)).where(self.model.c.id == obj_id)
        return await self.db.execute(query=query)

    async def delete(self, obj_id: int) -> None:
        query = self.model.delete().where(self.model.c.id == obj_id)
        return await self.db.execute(query=query)



