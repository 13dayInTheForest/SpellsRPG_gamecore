from fastapi import APIRouter
from .v1.pistures.custom_pictures import router as custom_pictures
from .v1.pistures.profile_pictures import router as profile_pictures
from .v1.users.users_endpoint import router as users_endpoint


api_v1 = APIRouter(
    prefix='/v1'
)

api_v1.include_router(custom_pictures)
api_v1.include_router(profile_pictures)
api_v1.include_router(users_endpoint)
