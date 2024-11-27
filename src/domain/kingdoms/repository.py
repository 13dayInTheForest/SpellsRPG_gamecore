from abc import abstractmethod, ABC
from .schemas import *


class IKingdomsRepo(ABC):
    @abstractmethod
    async def create(self, kingdom: CreateKingdomSchema) -> int:
        pass

    @abstractmethod
    async def read(self, kingdom_id: int) -> KingdomSchema:
        pass

    @abstractmethod
    async def read_by_group_id(self, group_id: str) -> KingdomSchema:
        pass

    @abstractmethod
    async def update(self, kingdom_id: int, kingdom_updates: UpdateKingdomSchema) -> None:
        pass

    @abstractmethod
    async def delete(self, kingdom_id: int) -> None:
        pass
