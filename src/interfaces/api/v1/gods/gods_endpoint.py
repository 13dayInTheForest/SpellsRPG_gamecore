from fastapi import APIRouter, Request, Depends, Body
from src.domain.gods.schemas import *
from src.domain.gods.service import GodsService

from src.application.gods.usecase import GodsUseCase


router = APIRouter(
    prefix='/gods',
    tags=['Gods']
)


@router.post('/create')
async def create_god(god: CreateGodSchema) -> GodsSchema:
    service = GodsService()
    return await service.create(god)


@router.get('/get/{god_id}')
async def get_god_by_id(god_id: str) -> GodsSchema:
    service = GodsService()
    return await service.read(god_id)


@router.get('/get_one')
async def get_one_by_fields(fields: GodsQueryFilters = Depends()) -> GodsSchema:
    service = GodsService()
    return await service.read_one_by_fields(fields)


@router.get('/list')
async def get_many_by_fields(limit: int | None = 5, fields: GodsQueryFilters = Depends()) -> dict:
    service = GodsService()
    return await service.read_many_by_fields(fields, limit)


@router.patch('/update/{god_id}')
async def update_god(god_id: str, updates: UpdateGodsSchema) -> GodsSchema:
    service = GodsService()
    return await service.update(god_id, updates)


@router.delete('/delete/{god_id}')
async def delete_god(god_id: str) -> GodsSchema:
    service = GodsService()
    return await service.delete(god_id)


@router.post('/start_worshiping')
async def start_worshiping(telegram_id: str = Body(...), god_name: str = Body(...)):
    use_case = GodsUseCase()
    return await use_case.start_worshiping(telegram_id, god_name)


