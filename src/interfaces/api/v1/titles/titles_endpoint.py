from fastapi import APIRouter
from src.domain.titles.schemas import *
from src.domain.titles.service import TitlesService


router = APIRouter(
    prefix='/titles',
    tags=['Titles']
)


@router.post('/')
async def create_god(kingdom: CreateTitleSchema) -> TitlesSchema:
    service = TitlesService()
    return await service.create(kingdom)


@router.get('/{title_id}')
async def get_kingdom_by_id(title_id: int) -> TitlesSchema:
    service = TitlesService()
    return await service.read(title_id)


@router.patch('/{title_id}')
async def update_kingdom(title_id: int, updates: CreateTitleSchema) -> TitlesSchema:
    service = TitlesService()
    return await service.update(title_id, updates)


@router.delete('/{title_id}')
async def delete_kingdom(title_id: int) -> TitlesSchema:
    service = TitlesService()
    return await service.delete(title_id)
