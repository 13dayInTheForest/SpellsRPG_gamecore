from abc import ABC, abstractmethod
from src.schemas.pic_schemas import CreatePicRequest


class IAIPictureService(ABC):
    @abstractmethod
    async def get_picture(self, prompt: CreatePicRequest) -> str:
        pass

