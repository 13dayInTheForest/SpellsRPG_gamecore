from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Dict, Any, Type
from pydantic import BaseModel


class BaseRepo:
    def __init__(self,
                 collection: AsyncIOMotorCollection,
                 schema: Type[BaseModel]
                 ):
        self.collection = collection
        self.schema = schema

    async def create(self, document: Type[BaseModel]) -> str:
        result = await self.collection.insert_one(document.dict())
        return result.inserted_id

    async def find_one_by_id(self, obj_id: str) -> Type[BaseModel] | None:
        result = await self.collection.find_one({'_id': obj_id})
        return self.schema(**result) if result is not None else None

    async def find_one_by_filter(self, doc_filter: Dict[str, Any]) -> Type[BaseModel] | None:
        result = await self.collection.find_one(doc_filter)
        return self.schema(**result) if result is not None else None

    async def find_many_by_filter(self, doc_filter: Type[BaseModel], limit: int = 5) -> List[Dict[str, Any]]:
        cursor = self.collection.find(doc_filter.dict(exclude_none=True))
        return await cursor.to_list(length=limit)

    async def update(self, obj_id: str, update: Type[BaseModel]) -> None:
        await self.collection.update_one(
            {'_id': obj_id},
            {'$set': update.dict()}
        )

    async def delete(self, obj_id: str) -> None:
        await self.collection.delete_one({'_id': obj_id})

    async def get_collection_len(self) -> int:
        return await self.collection.estimated_document_count()

