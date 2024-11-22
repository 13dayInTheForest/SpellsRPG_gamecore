from abc import abstractmethod, ABC
from .schemas import CreateUserSchema, UserSchema, UpdateUserSchema


class IUsersRepo(ABC):
    @abstractmethod
    async def create(self, user: CreateUserSchema) -> int:
        pass

    @abstractmethod
    async def read(self, user_id: int) -> UserSchema:
        pass

    @abstractmethod
    async def read_by_telegram_id(self, telegram_id: str) -> UserSchema:
        pass

    @abstractmethod
    async def update(self, user_id: int, user_updates: UpdateUserSchema) -> None:
        pass

    @abstractmethod
    async def delete(self, user_id: int) -> None:
        pass
