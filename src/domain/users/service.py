from fastapi import HTTPException
from .repository import IUsersRepo
from .schemas import *
from src.infrastructure.di.repo_container import RepoContainer


class UserService:
    def __init__(self):
        self.repo: IUsersRepo = RepoContainer.user_repo()

    async def create_user(self, user: CreateUserSchema) -> UserSchema:
        user = CreateUserSchemaForDB(**user.dict())
        user_id = await self.repo.create(user)
        return await self.repo.read(user_id)

    async def find_user_by_id(self, user_id: int) -> UserSchema:
        user = await self.repo.read(user_id)
        if user is None:
            raise HTTPException(status_code=404, detail=f'Not Found User with ID-{user_id}')
        return user

    async def update_user(self, user_id: int, user_updates: UpdateUserSchema) -> UserSchema:
        user = await self.find_user_by_id(user_id)
        await self.repo.update(user_id, user_updates)
        return user

    async def delete_user(self, user_id: int) -> UserSchema:
        user = await self.find_user_by_id(user_id)
        await self.repo.delete(user_id)
        return user

    async def find_user_by_telegram_id(self, telegram_id: int) -> UserSchema:
        user = await self.repo.read_by_telegram_id(telegram_id)
        if user is None:
            raise HTTPException(status_code=404, detail=f'Not Found User with Telegram ID-{telegram_id}')
        return user

