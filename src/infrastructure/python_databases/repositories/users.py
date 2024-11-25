from src.domain.users.repository import IUsersRepo
from src.domain.users.schemas import UserSchema
from .base import BaseRepo


class UserRepo(BaseRepo, IUsersRepo):
    async def read_by_telegram_id(self, telegram_id: str) -> UserSchema:
        query = self.model.select().where(self.model.c.telegram_id == telegram_id)
        response = await self.db.fetch_one(query=query)
        return UserSchema(**dict(response)) if response is not None else None


