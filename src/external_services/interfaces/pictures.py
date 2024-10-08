from abc import ABC, abstractmethod


class IAIPictureService(ABC):
    @abstractmethod
    async def get_picture(self, prompt: str) -> str:
        pass

