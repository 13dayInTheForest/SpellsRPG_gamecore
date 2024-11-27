from fastapi import HTTPException
from .repository import IKingdomsRepo
from .schemas import *
from src.infrastructure.di.repo_container import RepoContainer


class KingdomsService:
    repo: IKingdomsRepo

    def __init__(self):
        self.repo = RepoContainer.kingdoms_repo()

    async def create(self, kingdom: CreateKingdomSchema) -> KingdomSchema:
        if not kingdom.group_id.isdigit():
            raise HTTPException(status_code=409, detail=f'Group id must be Integer')
        if await self.repo.read_by_group_id(kingdom.group_id):
            raise HTTPException(status_code=409, detail=f'Group id is already taken')
        kingdom_id = await self.repo.create(kingdom)
        return await self.repo.read(kingdom_id)

    async def read(self, kingdom_id: int) -> KingdomSchema:
        kingdom = await self.repo.read(kingdom_id)
        if kingdom is None:
            raise HTTPException(status_code=404, detail=f'Not Found Title with ID-{kingdom_id}')
        return kingdom

    async def update(self, kingdom_id: int, kingdom_updates: UpdateKingdomSchema) -> KingdomSchema:
        kingdom = await self.read(kingdom_id)
        await self.repo.update(kingdom_id, kingdom_updates)
        return kingdom

    async def delete(self, kingdom_id: int) -> KingdomSchema:
        kingdom = await self.read(kingdom_id)
        await self.repo.delete(kingdom_id)
        return kingdom

