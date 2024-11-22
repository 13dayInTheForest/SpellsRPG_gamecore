from ..python_databases.repositories import *
from src.infrastructure.python_databases.database import database
from src.infrastructure.python_databases.models.users import users
from src.domain.users.schemas import UserSchema


class RepoContainer:
    @staticmethod
    def user_repo():
        return UserRepo(database, users, UserSchema)

