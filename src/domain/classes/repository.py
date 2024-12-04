from abc import ABC, abstractmethod
from typing import Dict, Any, List
from src.domain.classes.schemas import *


class IClassesRepo(ABC):
    @abstractmethod
    async def create(self, document: CreateClassesSchema) -> str:
        pass

    @abstractmethod
    async def find_one_by_id(self, class_id: str) -> ClassesSchema:
        pass

    @abstractmethod
    async def find_one_by_filter(self, doc_filter: Dict[str, Any]) -> ClassesSchema:
        pass

    @abstractmethod
    async def find_many_by_filter(self, doc_filter: Dict[str, Any], limit: int =5) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def update(self, class_id: str, update: UpdateClassesSchema) -> None:
        pass

    @abstractmethod
    async def delete(self, class_id: str) -> None:
        pass

    @abstractmethod
    async def get_collection_len(self) -> int:
        pass
