from .repository import IClassesRepo
from src.infrastructure.di.repo_container import RepoContainer
from .schemas import *
from fastapi import HTTPException


class GodsService:
    repo: IClassesRepo

    def __init__(self):
        self.repo = RepoContainer.classes_repo()

    async def create(self, class_: CreateClassesSchema) -> ClassesSchema:
        class_id = await self.repo.create(class_)
        return await self.repo.find_one_by_id(class_id)

    async def read(self, class_id: str) -> ClassesSchema:
        if len(class_id) != 24:
            raise HTTPException(status_code=400, detail=f'{class_id} is not a valid ObjectId')

        class_ = await self.repo.find_one_by_id(class_id)
        if class_ is None:
            raise HTTPException(status_code=404, detail=f'Not Found Class with id-{class_id}')
        return class_

    async def read_one_by_fields(self, fields: ClassQueryFilters) -> ClassesSchema:
        fields = fields.dict(exclude_none=True)
        if not fields:
            raise HTTPException(status_code=404, detail=f'Class Not Found')

        class_ = await self.repo.find_one_by_filter(fields)
        if class_ is None:
            raise HTTPException(status_code=404, detail=f'Not Found Class with fields-{fields}')
        return class_

    async def read_many_by_fields(self, fields: ClassQueryFilters, limit: int) -> dict:
        classes = await self.repo.find_many_by_filter(fields.dict(exclude_none=True), limit)
        return {'result': classes}

    async def update(self, class_id: str, updates: UpdateClassesSchema) -> ClassesSchema:
        await self.read(class_id)
        await self.repo.update(class_id, updates)
        return await self.repo.find_one_by_id(class_id)

    async def delete(self, class_id: str) -> ClassesSchema:
        god = await self.read(class_id)
        await self.repo.delete(class_id)
        return god
