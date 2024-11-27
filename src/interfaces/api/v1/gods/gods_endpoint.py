from fastapi import APIRouter, Request
from src.domain.gods.schemas import *
from src.domain.gods.service import GodsService


router = APIRouter(
    prefix='/gods',
    tags=['Gods']
)


@router.post('/')
async def create_god(god: CreateGodSchema) -> GodsSchema:
    service = GodsService()
    return await service.create(god)


@router.get('/{god_id}')
async def get_god_by_id(god_id: str) -> GodsSchema:
    service = GodsService()
    return await service.read(god_id)


@router.get('/get_one')
async def get_one_by_fields(request: Request) -> GodsSchema:
    service = GodsService()
    query_params = dict(request.query_params)
    return await service.read_one_by_fields(query_params)


@router.get('/get_list')
async def get_many_by_fields(request: Request) -> List[Dict[str, Any]]:
    service = GodsService()
    query_params = dict(request.query_params)
    limit = query_params.pop('limit') if query_params.get('limit') else 5
    return await service.read_many_by_fields(query_params, limit)


@router.patch('/{god_id}')
async def update_god(god_id: str, updates: UpdateGodsSchema) -> GodsSchema:
    service = GodsService()
    return await service.update(god_id, updates)


@router.delete('/{god_id}')
async def delete_god(god_id: str) -> GodsSchema:
    service = GodsService()
    return await service.delete(god_id)
