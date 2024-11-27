from abc import abstractmethod, ABC
from .schemas import CreateTitleSchema, TitlesSchema


class ITitleRepo(ABC):
    @abstractmethod
    async def create(self, title: CreateTitleSchema) -> int:
        pass

    @abstractmethod
    async def read(self, title_id: int) -> TitlesSchema:
        pass

    @abstractmethod
    async def update(self, title_id: int, title_updates: CreateTitleSchema) -> None:
        pass

    @abstractmethod
    async def delete(self, title_id: int) -> None:
        pass
