from fastapi.responses import FileResponse

from src.core.config import settings
from src.core.interfaces.cloud_stogare_interface import ICloudStorage
from src.core.interfaces.pictures_interface import IAIPictureService
from src.external_services.cloud_storage.gcs_service import GoogleCloudStorageService
from src.external_services.pictures import FluxFreeAIPictureService
from src.schemas.pic_schemas import CreatePicRequest, PicDetail
from src.utils.image_utils import get_picture_from_url


class PictureService:
    style = settings.DEFAULT_STYLE

    def __init__(self):
        self._ai_service: IAIPictureService = FluxFreeAIPictureService()
        self._cloud_service: ICloudStorage = GoogleCloudStorageService()

    async def generate(self, request: CreatePicRequest) -> PicDetail:
        request.prompt += self.style
        return await self._ai_service.get_picture(request)


class ProfilePictureService(PictureService):
    style = settings.PROFILE_STYLE_PROMPT

    async def save(self, detail: PicDetail):
        image = await get_picture_from_url(detail.url)
        print(image)
        response = await self._cloud_service.add(
            bucket_name='spells_pictures/profile_pictures',
            file_data=image,
            blob_name=f'{detail.user}-avatar'
        )
        return {'detail': response}

