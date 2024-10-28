from fastapi import APIRouter
from src.api.pistures.profile_pictures import router as profile_router
from src.api.pistures.custom_pictures import router as custom_router


pictures_router = APIRouter()
pictures_router.include_router(profile_router, tags=['profile'])
pictures_router.include_router(custom_router, tags=['custom'])
