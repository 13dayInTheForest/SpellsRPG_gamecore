from .repository import ISkillsRepo
from src.infrastructure.di.repo_container import RepoContainer
from .schemas import *
from fastapi import HTTPException


class GodsService:
    repo: ISkillsRepo

    def __init__(self):
        self.repo = RepoContainer.skills_repo()

    async def create(self, skill: CreateSkillsSchema) -> SkillsSchema:
        if await self.repo.find_one_by_filter({'name': skill.name}):
            raise HTTPException(status_code=400, detail=f'Skill with name {skill.name} already exists')
        skill_id = await self.repo.create(skill)
        return await self.repo.find_one_by_id(skill_id)

    async def read(self, skill_id: str) -> SkillsSchema:
        if len(skill_id) != 24:
            raise HTTPException(status_code=400, detail=f'{skill_id} is not a valid ObjectId')

        skill = await self.repo.find_one_by_id(skill_id)
        if skill is None:
            raise HTTPException(status_code=404, detail=f'Not Found Skill with id-{skill_id}')
        return skill

    async def read_one_by_fields(self, fields: SkillsQueryFilters) -> SkillsSchema:
        fields = fields.dict(exclude_none=True)
        if not fields:
            raise HTTPException(status_code=404, detail=f'Skill Not Found')

        skill = await self.repo.find_one_by_filter(fields)
        if skill is None:
            raise HTTPException(status_code=404, detail=f'Not Found Skill with fields-{fields}')
        return skill

    async def read_many_by_fields(self, fields: SkillsQueryFilters, limit: int) -> dict:
        skills = await self.repo.find_many_by_filter(fields.dict(exclude_none=True), limit)
        return {'result': skills}

    async def update(self, skill_id: str, updates: UpdateSkillsSchema) -> SkillsSchema:
        await self.read(skill_id)
        await self.repo.update(skill_id, updates)
        return await self.repo.find_one_by_id(skill_id)

    async def delete(self, skill_id: str) -> SkillsSchema:
        skill = await self.read(skill_id)
        await self.repo.delete(skill_id)
        return skill

    async def read_or_none(self, skill_id: str) -> SkillsSchema | None:
        if len(skill_id) != 24:
            return None
        skill = await self.repo.find_one_by_id(skill_id)
        if skill is None:
            return None
        return skill
