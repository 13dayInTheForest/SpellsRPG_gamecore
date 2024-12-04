from .base import BaseRepo
from src.domain.characters.repository import ICharacterRepo


class CharacterRepo(BaseRepo, ICharacterRepo):
    async def find_character_by_telegram_id(self, telegram_id: str):
        query = self.model.select().where(self.model.c.telegram_user_id == telegram_id)
        response = await self.db.fetch_one(query=query)
        print(dict(response))
        return self.schema(**dict(response)) if response is not None else None
