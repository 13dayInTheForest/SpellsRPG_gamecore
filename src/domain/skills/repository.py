from abc import ABC, abstractmethod
from typing import Dict, Any, List
from .schemas import *


class ISkillsRepo(ABC):
    @abstractmethod
    async def create(self, document: CreateSkillsSchema) -> str:
        pass

    @abstractmethod
    async def find_one_by_id(self, skill_id: str) -> SkillsSchema:
        pass

    @abstractmethod
    async def find_one_by_filter(self, doc_filter: Dict[str, Any]) -> SkillsSchema:
        pass

    @abstractmethod
    async def find_many_by_filter(self, doc_filter: Dict[str, Any], limit: int =5) -> List[Dict[str, Any]]:
        pass

    @abstractmethod
    async def update(self, skill_id: str, update: UpdateSkillsSchema) -> None:
        pass

    @abstractmethod
    async def delete(self, skill_id: str) -> None:
        pass

    @abstractmethod
    async def get_collection_len(self) -> int:
        pass
