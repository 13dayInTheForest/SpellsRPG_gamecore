from fastapi import UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from src.infrastructure.config import settings
from src.domain.pictures.cloud_storage import ICloudStorage
from src.domain.pictures.ai_pictures import IAIPictureService
from src.domain.pictures.schemas import CreatePicRequest, PicDetail
from src.di.pic_container import PicContainer


class PictureService:
    style = settings.DEFAULT_STYLE_PROMPT
    bucket = 'spells_pictures'
    blob = 'stuff'
    pic_type = ''

    def __init__(self):
        self._ai_service: IAIPictureService = PicContainer.ai_picture_service()
        self._cloud_service: ICloudStorage = PicContainer.cloud_service()

    async def generate(self, request: CreatePicRequest) -> PicDetail:
        request.prompt += self.style
        return await self._ai_service.get_picture(request)

    async def save(self, picture: UploadFile, user_id):
        if picture.content_type != "image/jpeg":
            raise HTTPException(status_code=400, detail="Only JPG files are allowed")

        image = await picture.read()
        response = await self._cloud_service.add_file(
            bucket_name='spells_pictures',
            file_data=image,
            blob_name=f'{self.blob}/{user_id}-{self.pic_type}.jpg'
        )
        return {'detail': response}

    async def get(self, user_id: int):
        image = await self._cloud_service.fetch_file(
                self.bucket,
                f'{self.blob}/{user_id}-{self.pic_type}.jpg'
            ),
        return StreamingResponse(image, media_type='image/jpg')

    async def delete(self, user_id: int):
        return await self._cloud_service.delete_file(
            bucket_name=self.bucket,
            blob_name=f'{self.blob}/{user_id}-{self.pic_type}.jpg'
        )


class ProfilePictureService(PictureService):
    style = settings.PROFILE_STYLE_PROMPT
    blob = 'profile_pictures'
    pic_type = 'avatar'


class CustomPictureService(PictureService):
    style = ''
    blob = 'stuff'
    pic_type = 'stuff'

