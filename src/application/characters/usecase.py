from fastapi import HTTPException
from datetime import datetime

from src.domain.users.service import UserService
from src.domain.users.schemas import UpdateUserSchema
from src.domain.characters.service import CharacterService
from src.domain.characters.schemas import CreateCharacterSchemaForDB, CreateCharacterSchema, CharacterSchema
from src.domain.gods.service import GodsService

from src.application.utils.changes import apply_effects


class CharacterUseCase:
    def __init__(self):

        self.user_service = UserService()
        self.characters_service = CharacterService()
        self.god_service = GodsService()

    async def create_character(self, info: CreateCharacterSchema) -> CharacterSchema:
        user = await self.user_service.find_user_by_telegram_id(info.telegram_user_id)
        if not user.can_create_characters or not user.can_play:
            raise HTTPException(status_code=403, detail=f'Current user-{user.telegram_id} can not create characters')
        if user.current_character_id:
            raise HTTPException(status_code=403, detail=f'Current user-{user.telegram_id} already have a character')

        info = CreateCharacterSchemaForDB(**info.dict())
        character = await self.characters_service.create_character(info)
        await self.user_service.update_user(user.id, UpdateUserSchema(current_character_id=character.id))
        return character

    async def get_character_info(self, telegram_id: str) -> CharacterSchema:
        character = await self.characters_service.find_character_by_telegram_id(telegram_id)
        character.born_date = (datetime.now() - character.born_date).days + 18
        god = await self.god_service.read(character.god_id)

        character = character.copy(update=apply_effects(character, god.changes).dict(exclude_none=True))

        return character


