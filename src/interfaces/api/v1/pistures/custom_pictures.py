from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from src.domain.pictures.schemas import CreatePicRequest
from src.application.pictures.service import CustomPictureService
from src.utils.image_utils import get_picture_from_url
from .profile_pictures import create_profile_pic


router = APIRouter(
    prefix='/pic/custom',
    tags=['pictures']
)


@router.get('/show_profile')
async def show_picture_by_link(prompt: str):
    picture = await create_profile_pic(CreatePicRequest(username='test', prompt=prompt))
    img = await get_picture_from_url(picture.url)
    return StreamingResponse(
        iter([img]),
        media_type='image/jpeg')


@router.get('/show')
async def show_picture_by_link(prompt: str):
    service = CustomPictureService()
    picture = await service.generate(CreatePicRequest(username='test', prompt=prompt))
    img = await get_picture_from_url(picture.url)
    return StreamingResponse(
        iter([img]),
        media_type='image/jpeg')
