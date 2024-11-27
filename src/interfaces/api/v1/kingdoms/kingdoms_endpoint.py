from fastapi import APIRouter, Request
from src.domain.kingdoms.schemas import *
from src.domain.kingdoms.service import KingdomsService


router = APIRouter(
    prefix='/kingdoms',
    tags=['Kingdoms']
)

''' НУЖНО ПЕРЕПИСАТЬ НА ЮЗКЕЙСЫ '''
@router.post('/')
async def create_kingdom(kingdom: CreateKingdomSchema) -> KingdomSchema:
    service = KingdomsService()
    return await service.create(kingdom)


@router.get('/{kingdom_id}')
async def get_kingdom_by_id(kingdom_id: int) -> KingdomSchema:
    service = KingdomsService()
    return await service.read(kingdom_id)


# @router.get('/get_many_by_filter/{kingdom_id}')
# async def get_kingdom_by_id(kingdom_id: str, request: Request) -> KingdomSchema:
#     query_filter = dict(request.query_params)
#     service = KingdomsService()
#     return await service.read(kingdom_id)


@router.patch('/{kingdom_id}')
async def update_kingdom(kingdom_id: int, updates: UpdateKingdomSchema) -> KingdomSchema:
    service = KingdomsService()
    return await service.update(kingdom_id, updates)


@router.delete('/{kingdom_id}')
async def delete_kingdom(kingdom_id: int) -> KingdomSchema:
    service = KingdomsService()
    return await service.delete(kingdom_id)
