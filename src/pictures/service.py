from fastapi import UploadFile, HTTPException
from fastapi.responses import StreamingResponse
from src.core.config import settings
from src.core.interfaces.cloud_storage import ICloudStorage
from src.core.interfaces.ai_pictures import IAIPictureService
from src.external_services.cloud_storage.gcs_service import GoogleCloudStorageService
from src.external_services.pictures import FluxFreeAIPictureService
from src.pictures.schemas import CreatePicRequest, PicDetail


class PictureService:
    style = settings.DEFAULT_STYLE_PROMPT
    bucket = 'spells_pictures'
    blob = 'stuff'

    def __init__(self):
        self._ai_service: IAIPictureService = FluxFreeAIPictureService()
        self._cloud_service: ICloudStorage = GoogleCloudStorageService()

    async def generate(self, request: CreatePicRequest) -> PicDetail:
        request.prompt += self.style
        return await self._ai_service.get_picture(request)

    async def save(self, picture: UploadFile, user_id):
        print(self.bucket, f'{self.blob}/{user_id}.jpg')
        print(await self._cloud_service.exist(self.bucket, f'{self.blob}/{user_id}.jpg'))
        if await self._cloud_service.exist(self.bucket, f'{self.blob}/{user_id}.jpg'):
            print('exist')
            return self._cloud_service.exist(self.bucket, f'{self.blob}/{user_id}.jpg')
        if picture.content_type != "image/jpeg":
            raise HTTPException(status_code=400, detail="Only JPG files are allowed")

        image = await picture.read()
        response = await self._cloud_service.add(
            bucket_name='spells_pictures',
            file_data=image,
            blob_name=f'{self.blob}/{user_id}-avatar.jpg'
        )
        return {'detail': response}

    async def get(self, user_id: int):
        image = await self._cloud_service.fetch(
                self.bucket,
                f'{self.blob}/{user_id}-avatar.jpg'
            ),
        return StreamingResponse(image, media_type='image/jpg')


class ProfilePictureService(PictureService):
    style = settings.PROFILE_STYLE_PROMPT
    blob = 'profile_pictures'


class CustomPictureService(PictureService):
    style = ''
    blob = 'stuff'

