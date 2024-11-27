from src.domain.kingdoms.repository import IKingdomsRepo
from src.domain.kingdoms.schemas import KingdomSchema
from .base import BaseRepo


class KingdomRepo(BaseRepo, IKingdomsRepo):
    async def read_by_group_id(self, group_id: str) -> KingdomSchema | None:
        query = self.model.select().where(self.model.c.group_id == group_id)
        response = await self.db.fetch_one(query=query)
        return KingdomSchema(**dict(response)) if response is not None else None
