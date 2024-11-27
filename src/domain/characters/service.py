from fastapi import HTTPException
from .repository import ICharacterRepo
from .schemas import *
from src.infrastructure.di.repo_container import RepoContainer
from random import randint


class CharacterService:
    def __init__(self):
        self.repo: ICharacterRepo = RepoContainer.characters_repo()

    async def create_character(self, character: CreateCharacterSchemaForDB) -> CharacterSchema:
        """
        Этот метод не вызывается напрямую.
        Для корректной работы сюда передается CreateCharacterSchemaForDB
        с уже заполненными полями внешних ключей.
        """
        character.hp = randint(10, 1000)
        character.max_age = randint(20, 100)
        character.gold = randint(5, 1_000)
        character.karma = randint(0, 20)
        character.strength = randint(0, 20)
        character.mana = randint(0, 20)

        if character.karma < 5 and character.mana < 5 and character.strength < 5:
            #  Если человеку не повезло, то дается дополнительные очки прокачки
            character.exp_points = 20

        character_id = await self.repo.create(character)
        return await self.repo.read(character_id)

    async def find_character_by_id(self, character_id: int) -> CharacterSchema:
        character = await self.repo.read(character_id)
        if character is None:
            raise HTTPException(status_code=404, detail=f'Not found character with id-{character_id}')
        return character

    async def update_character(self, character_id: int, user_updates: UpdateCharacterSchema) -> CharacterSchema:
        await self.find_character_by_id(character_id)
        await self.repo.update(character_id, user_updates)
        return await self.repo.read(character_id)

    async def delete_character(self, character_id: int) -> CharacterSchema:
        character = await self.find_character_by_id(character_id)
        await self.repo.delete(character_id)
        return character
