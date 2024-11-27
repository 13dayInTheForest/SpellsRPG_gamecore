from abc import ABC, abstractmethod
from typing import Dict, Any, List
from src.domain.gods.schemas import GodsSchema, UpdateGodsSchema, CreateGodSchema


class IGodsRepo(ABC):
    @abstractmethod
    async def create(self, document: CreateGodSchema) -> str:
        pass

    @abstractmethod
    async def find_one_by_id(self, god_id: str) -> GodsSchema:
        pass

    @abstractmethod
    async def find_one_by_filter(self, doc_filter: Dict[str, Any]) -> GodsSchema:
        pass

    @abstractmethod
    async def find_many_by_filter(self, doc_filter: Dict[str, Any], limit: int =5) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def update(self, god_id: str, update: UpdateGodsSchema) -> None:
        pass

    @abstractmethod
    async def delete(self, god_id: str) -> None:
        pass

    @abstractmethod
    async def get_collection_len(self) -> int:
        pass
