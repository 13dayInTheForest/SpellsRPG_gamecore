from fastapi import HTTPException

from src.domain.characters.service import CharacterService
from src.domain.characters.schemas import *
from src.domain.gods.service import GodsService
from src.domain.gods.schemas import GodsSchema, GodsQueryFilters

from src.application.utils.requirements import check_needs
from src.application.utils.changes import apply_effects


class GodsUseCase:
    def __init__(self):
        self.characters_service = CharacterService()
        self.god_service = GodsService()

    # Возвращает измененные поля
    async def start_worshiping(self, telegram_id: str, god_name: str) -> CharacterSchema:
        god = await self.god_service.read_one_by_fields(GodsQueryFilters(name=god_name))
        if not god.active:
            raise HTTPException(status_code=403, detail=f'God {god.name} is not active now')

        character = await self.characters_service.find_character_by_telegram_id(telegram_id)

        if character.god_id is not None:
            raise HTTPException(status_code=403, detail=f'User {telegram_id} already have a god')
        if not check_needs(character, god.needs, god.needs_count):
            raise HTTPException(status_code=403, detail=f'User {telegram_id} can not start worshiping to {god.name}')

        characters_updates = apply_effects(character, god.changes)
        characters_updates.god_id = god.id

        return await self.characters_service.update_character(
            character.id,
            UpdateCharacterSchema(**characters_updates.dict())
        )

    async def stop_worshiping(self, telegram_id: str) -> CharacterSchema:
        character = await self.characters_service.find_character_by_telegram_id(telegram_id)
        god = await self.god_service.read_or_none(character.god_id)
        characters_updates = apply_effects(character, god.to_stop)
        characters_updates = characters_updates.dict()
        characters_updates.pop('id')
        characters_updates['god_id'] = None

        return await self.characters_service.update_fields(
            character.id,
            characters_updates
        )





