from src.domain.users.repository import IUsersRepo
from src.domain.users.schemas import UserSchema
from src.infrastructure.python_databases.models.users import users
from .base import BaseRepo


class UserRepo(BaseRepo, IUsersRepo):
    async def read_by_telegram_id(self, telegram_id: str) -> UserSchema:
        query = self.model.select().where(self.model.c.telegram_id == telegram_id)
        response = await self.db.execute(query=query)
        return UserSchema(**response)


