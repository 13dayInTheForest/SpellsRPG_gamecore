from fastapi import APIRouter, UploadFile, File

from src.pictures.schemas import CreatePicRequest, PicDetail
from src.pictures.service import ProfilePictureService

router = APIRouter(
    prefix='/profile'
)


@router.post('/create')
async def create_profile_pic(prompt: CreatePicRequest) -> PicDetail:
    pic_manager = ProfilePictureService()
    return await pic_manager.generate(prompt)


@router.post('/save/{id}')
async def save_profile_pic(user_id: int, picture: UploadFile = File(...)):
    pic_manager = ProfilePictureService()
    return await pic_manager.save(picture, user_id)


@router.get('/get/{user_id}')
async def get_profile_pic(user_id: int):
    pic_manager = ProfilePictureService()
    return await pic_manager.get(user_id)


@router.delete('/delete/{user_id}')
async def update_profile_pic(user_id: int):
    pic_manager = ProfilePictureService()
    return await pic_manager.delete(user_id)
