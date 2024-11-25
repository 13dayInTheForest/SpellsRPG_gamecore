from .base import BaseRepo
from src.domain.characters.repository import ICharacterRepo


class CharacterRepo(BaseRepo, ICharacterRepo):
    pass
