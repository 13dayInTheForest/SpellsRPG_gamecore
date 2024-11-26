from src.infrastructure.python_databases.repositories import *
from src.infrastructure.python_databases.database import database
from src.infrastructure.python_databases.models import *
from src.domain.users.schemas import UserSchema
from src.domain.characters.schemas import CharacterSchema


class RepoContainer:
    @staticmethod
    def user_repo():
        return UserRepo(database, users, UserSchema)

    @staticmethod
    def character_repo():
        return CharacterRepo(database, characters, CharacterSchema)
