from .repository import IGodsRepo
from src.infrastructure.di.repo_container import RepoContainer
from .schemas import *
from fastapi import HTTPException


class GodsService:
    repo: IGodsRepo

    def __init__(self):
        self.repo = RepoContainer.gods_repo()

    async def create(self, god: CreateGodSchema) -> GodsSchema:
        god_id = await self.repo.create(god)
        return await self.repo.find_one_by_id(god_id)

    async def read(self, god_id: str) -> GodsSchema:
        if len(god_id) != 24:
            raise HTTPException(status_code=400, detail=f'{god_id} is not a valid ObjectId')

        god = await self.repo.find_one_by_id(god_id)
        if god is None:
            raise HTTPException(status_code=404, detail=f'Not Found God with id-{god_id}')
        return god

    async def read_one_by_fields(self, fields: GodsQueryFilters) -> GodsSchema:
        fields = fields.dict(exclude_none=True)
        if not fields:
            raise HTTPException(status_code=404, detail=f'God Not Found')

        god = await self.repo.find_one_by_filter(fields)
        if god is None:
            raise HTTPException(status_code=404, detail=f'Not Found God with fields-{fields}')
        return god

    async def read_many_by_fields(self, fields: GodsQueryFilters, limit: int) -> dict:
        gods = await self.repo.find_many_by_filter(fields.dict(exclude_none=True), limit)
        return {'result': gods}

    async def update(self, god_id: str, updates: UpdateGodsSchema) -> GodsSchema:
        await self.read(god_id)
        await self.repo.update(god_id, updates)
        return await self.repo.find_one_by_id(god_id)

    async def delete(self, god_id: str) -> GodsSchema:
        god = await self.read(god_id)
        await self.repo.delete(god_id)
        return god
