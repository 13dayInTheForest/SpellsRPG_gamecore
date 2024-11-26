from abc import ABC, abstractmethod


class ICharacterService(ABC):
    @abstractmethod
    async def create_character(self, character: CreateCharacterSchemaForDB) -> CharacterSchema:
        pass
    
    @abstractmethod
    async def find_character_by_id(self, character_id: int) -> CharacterSchema:
        pass
    
    @abstractmethod
    async def update_character(self, character_id: int, user_updates: UpdateCharacterSchema) -> CharacterSchema:
        pass

    @abstractmethod
    async def delete_character(self, character_id: int) -> CharacterSchema:
        pass

