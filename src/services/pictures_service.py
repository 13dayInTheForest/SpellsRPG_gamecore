from fastapi.responses import FileResponse

from src.core.config import settings
from src.core.interfaces.pictures_interface import IAIPictureService
from src.external_services.pictures import FluxFreeAIPictureService
from src.schemas.pic_schemas import CreatePicRequest


class PictureService:
    style = settings.DEFAULT_STYLE

    def __init__(self):
        self._ai_service: IAIPictureService = FluxFreeAIPictureService()

    async def generate(self, request: CreatePicRequest):
        request.prompt += self.style
        return await self._ai_service.get_picture(request)


class ProfilePictureService(PictureService):
    style = settings.PROFILE_STYLE_PROMPT
