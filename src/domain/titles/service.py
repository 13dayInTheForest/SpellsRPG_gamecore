from fastapi import HTTPException
from .repository import ITitleRepo
from .schemas import *
from src.infrastructure.di.repo_container import RepoContainer


class TitlesService:
    repo: ITitleRepo

    def __init__(self):
        self.repo = RepoContainer.titles_repo()

    async def create(self, title: CreateTitleSchema) -> TitlesSchema:
        title_id = await self.repo.create(title)
        return await self.repo.read(title_id)

    async def read(self, title_id: int) -> TitlesSchema:
        title = await self.repo.read(title_id)
        if title is None:
            raise HTTPException(status_code=404, detail=f'Not Found Title with ID-{title_id}')
        return title

    async def update(self, title_id: int, title_updates: CreateTitleSchema) -> TitlesSchema:
        title = await self.read(title_id)
        await self.repo.update(title_id, title_updates)
        return title

    async def delete(self, title_id: int) -> TitlesSchema:
        title = await self.read(title_id)
        await self.repo.delete(title_id)
        return title

