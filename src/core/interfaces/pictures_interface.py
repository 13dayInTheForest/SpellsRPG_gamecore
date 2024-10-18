from abc import ABC, abstractmethod
from src.schemas.pic_schemas import CreatePicRequest, PicDetail


class IAIPictureService(ABC):
    @abstractmethod
    async def get_picture(self, prompt: CreatePicRequest) -> PicDetail:
        pass

