from fastapi import HTTPException
from .repository import ICharacterRepo
from .schemas import *
from src.infrastructure.di.repo_container import RepoContainer
from random import randint


class CharacterService:
    def __init__(self):
        self.repo: ICharacterRepo = RepoContainer.characters_repo()

    async def create_character(self, character: CreateCharacterSchemaForDB) -> CharacterSchema:
        character.hp = randint(50, 300)
        character.max_age = randint(20, 100)
        character.gold = randint(5, 1000)
        character.karma = randint(0, 20)
        character.strength = randint(0, 20)
        character.mana = randint(0, 20)

        if character.karma < 5 and character.mana < 5 and character.strength < 5:
            #  Если человеку не повезло, то дается дополнительные очки прокачки
            character.exp_points = 30
        elif character.karma == 0 and character.mana == 0 and character.strength == 0:
            character.exp_points = 100

        character_id = await self.repo.create(character)
        return await self.repo.read(character_id)

    async def find_character_by_id(self, character_id: int) -> CharacterSchema:
        character = await self.repo.read(character_id)
        if character is None:
            raise HTTPException(status_code=404, detail=f'Not found character with id-{character_id}')
        return character

    async def find_character_by_telegram_id(self, telegram_id: str) -> CharacterSchema:
        character = await self.repo.find_character_by_telegram_id(telegram_id)
        if character is None:
            raise HTTPException(status_code=404, detail=f'Not found character with telegram id-{telegram_id}')
        return character

    async def find_character_by_filter(self, character_filter: dict) -> CharacterSchema:
        pass

    async def update_character(self, character_id: int, user_updates: UpdateCharacterSchema) -> CharacterSchema:
        await self.find_character_by_id(character_id)
        await self.repo.update(character_id, user_updates)
        return await self.repo.read(character_id)

    async def delete_character(self, character_id: int) -> CharacterSchema:
        character = await self.find_character_by_id(character_id)
        await self.repo.delete(character_id)
        return character


