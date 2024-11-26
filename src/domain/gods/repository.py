from abc import ABC, abstractmethod
from typing import Dict, Any, List


class IGodsRepo(ABC):
    @abstractmethod
    async def create(self, document: Dict[str, Any]) -> str:
        pass

    @abstractmethod
    async def find_one_by_id(self, god_id: str) -> dict:
        pass

    @abstractmethod
    async def find_one_by_filter(self, doc_filter: Dict[str, Any]) -> Dict[str, Any]:
        pass

    @abstractmethod
    async def find_many_by_filter(self, doc_filter: Dict[str, Any], limit=5) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def update(self, god_id: str, update: Dict[str, Any]) -> None:
        pass

    @abstractmethod
    async def delete(self, god_id: str) -> None:
        pass

    @abstractmethod
    async def get_collection_len(self) -> int:
        pass
