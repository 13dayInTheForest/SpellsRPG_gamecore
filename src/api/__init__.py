from fastapi import APIRouter
from src.api.v1.endpoints.pictures_endpoint import router as pic_router


api_v1 = APIRouter(
    prefix='/v1'
)

api_v1.include_router(
    pic_router,
    prefix='/pic'
)