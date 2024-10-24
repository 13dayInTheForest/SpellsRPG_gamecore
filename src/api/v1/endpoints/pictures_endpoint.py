from fastapi import APIRouter, UploadFile, File
from fastapi.responses import StreamingResponse

from src.pictures.schemas import CreatePicRequest, PicDetail
from src.pictures.service import ProfilePictureService
from src.utils.image_utils import get_picture_from_url

router = APIRouter()


@router.post('/profile/create')
async def create_profile_pic(prompt: CreatePicRequest) -> PicDetail:
    pic_manager = ProfilePictureService()
    return await pic_manager.generate(prompt)


@router.get('/show')
async def show_picture_by_link(prompt: str):
    picture = await create_profile_pic(CreatePicRequest(username='test', prompt=prompt))
    img = await get_picture_from_url(picture.url)
    return StreamingResponse(
        iter([img]),
        media_type='image/jpeg')


@router.post('/profile/{id}/save')
async def save_profile_pic(user_id: int, picture: UploadFile = File(...)):
    pic_manager = ProfilePictureService()
    return await pic_manager.save(picture, user_id)


@router.get('/profile/get')
async def get_profile_pic(user_id: int):
    pic_manager = ProfilePictureService()
    return await pic_manager.get(user_id)