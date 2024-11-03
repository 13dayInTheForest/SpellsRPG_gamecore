from fastapi import APIRouter
from src.api.pistures import pictures_router


api_v1 = APIRouter(
    prefix='/v1'
)

api_v1.include_router(
    pictures_router,
    prefix='/pic',
    tags=['Pictures']
)