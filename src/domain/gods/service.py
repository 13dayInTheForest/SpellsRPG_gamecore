from .repository import IGodsRepo
from .schemas import *
from fastapi import HTTPException


class GodsService:
    def __init__(self, repo: IGodsRepo):
        self.repo = repo

    async def create(self, god: CreateGodSchema) -> GodsSchema:
        god_id = await self.repo.create(god.dict())
        return GodsSchema(**await self.repo.find_one_by_id(god_id))

    async def read(self, god_id: str) -> GodsSchema:
        god = await self.repo.find_one_by_id(god_id)
        if god is None:
            raise HTTPException(status_code=404, detail=f'Not Found God with id-{god_id}')
        return GodsSchema(**god)

    async def read_one_by_fields(self, fields: dict) -> GodsSchema:
        god = await self.repo.find_one_by_filter(fields)
        if god is None:
            raise HTTPException(status_code=404, detail=f'Not Found God with fields-{fields}')
        return GodsSchema(**god)

    async def read_many_by_fields(self, fields: dict) -> List[Dict]:
        gods = await self.repo.find_many_by_filter(fields)
        if not gods:
            raise HTTPException(status_code=404, detail=f'Not Found Gods with fields-{fields}')
        return gods

    async def update(self, god_id: str, updates: dict) -> GodsSchema:
        await self.repo.update(god_id, updates)
        return GodsSchema(**await self.repo.find_one_by_id(god_id))

    async def delete(self, god_id: str) -> GodsSchema:
        await self.repo.delete(god_id)
        return GodsSchema(**await self.repo.find_one_by_id(god_id))


