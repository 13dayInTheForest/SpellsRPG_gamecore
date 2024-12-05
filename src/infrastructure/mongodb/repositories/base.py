from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Dict, Any, Type, Optional
from pydantic import BaseModel
from bson import ObjectId


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
        result = await self.collection.find_one({'_id': ObjectId(obj_id)})
        if result is not None:
            result = dict(result)
            result['id'] = str(result.pop('_id'))
        return self.schema(**result) if result is not None else None

    async def find_one_by_filter(self, doc_filter: Dict[str, Any]) -> Type[BaseModel] | None:
        result = await self.collection.find_one(doc_filter)
        if result:
            result['id'] = str(result['_id'])
        print(result)
        return self.schema(**result) if result is not None else None

    async def find_many_by_filter(self,
                                  doc_filter: Dict[str, Any],
                                  limit: int = None
                                  ) -> List[Dict[str, Any]]:
        cursor = self.collection.find(doc_filter)
        result = await cursor.to_list(length=limit)
        for i in range(len(result)):
            result[i]['id'] = str(result[i].pop('_id'))

        return result

    async def update(self, obj_id: str, update: Type[BaseModel]) -> None:
        await self.collection.update_one(
            {'_id': ObjectId(obj_id)},
            {'$set': update.dict(exclude_none=True)}
        )

    async def delete(self, obj_id: str) -> None:
        await self.collection.delete_one({'_id': ObjectId(obj_id)})

    async def get_collection_len(self) -> int:
        return await self.collection.estimated_document_count()

