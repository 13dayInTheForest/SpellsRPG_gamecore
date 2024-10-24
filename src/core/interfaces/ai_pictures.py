from abc import ABC, abstractmethod
from src.pictures.schemas import CreatePicRequest, PicDetail


class IAIPictureService(ABC):
    @abstractmethod
    async def get_picture(self, prompt: CreatePicRequest) -> PicDetail:
        pass

