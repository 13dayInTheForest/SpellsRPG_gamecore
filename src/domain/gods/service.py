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
        god = await self.repo.find_one_by_id(god_id)
        if god is None:
            raise HTTPException(status_code=404, detail=f'Not Found God with id-{god_id}')
        return god

    async def read_one_by_fields(self, fields: Dict[str, Any]) -> GodsSchema:
        god = await self.repo.find_one_by_filter(fields)
        if god is None:
            raise HTTPException(status_code=404, detail=f'Not Found God with fields-{fields}')
        return god

    async def read_many_by_fields(self, fields: Dict[str, Any], limit: int = 5) -> List[Dict]:
        gods = await self.repo.find_many_by_filter(fields)
        if not gods:
            raise HTTPException(status_code=404, detail=f'Not Found Gods with fields-{fields}')
        return gods

    async def update(self, god_id: str, updates: UpdateGodsSchema) -> GodsSchema:
        await self.repo.update(god_id, updates)
        return await self.repo.find_one_by_id(god_id)

    async def delete(self, god_id: str) -> GodsSchema:
        await self.repo.delete(god_id)
        return await self.repo.find_one_by_id(god_id)


