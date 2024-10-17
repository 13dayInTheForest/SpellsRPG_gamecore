from fastapi import APIRouter
from fastapi.responses import StreamingResponse

from src.schemas.pic_schemas import CreatePicRequest
from src.services.pictures_service import ProfilePictureService
from src.utils.image_utils import get_picture_from_url

router = APIRouter()


@router.post('/create/profile_pic')
async def create_profile_pic(prompt: CreatePicRequest):
    pic_manager = ProfilePictureService()
    return await pic_manager.generate(prompt)


@router.get('/show')
async def show_picture_by_link(prompt: str):
    picture = await create_profile_pic(CreatePicRequest(username='test', prompt=prompt))
    img = await get_picture_from_url(picture.url)
    return StreamingResponse(
        iter([img]),
        media_type='image/jpeg'
    )

