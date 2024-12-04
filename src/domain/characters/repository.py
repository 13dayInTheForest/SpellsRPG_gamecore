from abc import abstractmethod, ABC
from .schemas import CreateCharacterSchemaForDB, UpdateCharacterSchema, CharacterSchema


class ICharacterRepo(ABC):
    @abstractmethod
    async def create(self, character: CreateCharacterSchemaForDB) -> int:
        pass

    @abstractmethod
    async def read(self, character_id: int) -> CharacterSchema:
        pass

    @abstractmethod
    async def update(self, character_id: int, user_updates: UpdateCharacterSchema) -> None:
        pass

    @abstractmethod
    async def delete(self, character_id: int) -> None:
        pass

    @abstractmethod
    async def find_character_by_telegram_id(self, telegram_id: str) -> CharacterSchema | None:
        pass

