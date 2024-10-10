from abc import ABC, abstractmethod


class IAIPictureManager(ABC):
    @abstractmethod
    async def get_picture(self, prompt: str) -> str:
        pass

