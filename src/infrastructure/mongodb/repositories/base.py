from motor.motor_asyncio import AsyncIOMotorCollection
from typing import List, Dict, Any


class BaseRepo:
    def __init__(self, collection: AsyncIOMotorCollection):
        self.collection = collection

    async def create(self, document: Dict[str, Any]) -> str:
        result = await self.collection.insert_one(document)
        return result.inserted_id

    async def find_one_by_id(self, obj_id: str) -> Dict[str, Any]:
        return await self.collection.find_one({'_id': obj_id})

    async def find_one_by_filter(self, doc_filter: Dict[str, Any]) -> Dict[str, Any]:
        return await self.collection.find_one(doc_filter)

    async def find_many_by_filter(self, doc_filter: Dict[str, Any], limit=5) -> List[Dict[str, Any]]:
        cursor = self.collection.find(doc_filter)
        return await cursor.to_list(length=limit)

    async def update(self, obj_id: str, update: Dict[str, Any]) -> None:
        await self.collection.update_one(
            {'_id': obj_id},
            {'$set': update}
        )

    async def delete(self, obj_id: str) -> None:
        await self.collection.delete_one({'_id': obj_id})

    async def get_collection_len(self) -> int:
        return await self.collection.estimated_document_count()

