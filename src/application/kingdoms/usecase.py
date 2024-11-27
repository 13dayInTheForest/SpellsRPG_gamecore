from fastapi import HTTPException

from src.domain.kingdoms.service import KingdomsService
from src.domain.kingdoms.schemas import *
from src.domain.users.service import UserService
from src.domain.characters.service import CharacterService


class KingdomUseCase:
    def __init__(self):
        self.kingdoms_service = KingdomsService()
        self.users_service = UserService()
        self.characters_service = CharacterService()

    async def create_kingdom(self, telegram_id: str, kingdom: CreateKingdomSchema) -> KingdomSchema:
        user = await self.users_service.find_user_by_telegram_id(telegram_id)
        if not user:
            raise HTTPException(status_code=404, detail=f'Cant find user with telegram id-{telegram_id}')
        if not user.can_create_kingdoms or not user.can_play:
            raise HTTPException(status_code=401, detail=f'{telegram_id} user cant do this')

        pass