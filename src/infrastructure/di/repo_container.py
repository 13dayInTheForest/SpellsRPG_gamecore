from src.infrastructure.python_databases.repositories import *

from src.infrastructure.python_databases.database import database
from src.infrastructure.python_databases.models import *

from src.infrastructure.mongodb.repositories import *
from src.infrastructure.mongodb.database import collections

from src.domain.users.schemas import UserSchema
from src.domain.characters.schemas import CharacterSchema
from src.domain.titles.schemas import TitlesSchema
from src.domain.kingdoms.schemas import KingdomSchema
from src.domain.gods.schemas import GodsSchema


class RepoContainer:
    @staticmethod
    def users_repo():
        return UserRepo(database, users, UserSchema)

    @staticmethod
    def characters_repo():
        return CharacterRepo(database, characters, CharacterSchema)

    @staticmethod
    def gods_repo():
        return GodsRepo(collections.get('gods'), GodsSchema)

    @staticmethod
    def titles_repo():
        return TitlesRepo(database, titles, TitlesSchema)

    @staticmethod
    def kingdoms_repo():
        return KingdomRepo(database, kingdoms, KingdomSchema)

