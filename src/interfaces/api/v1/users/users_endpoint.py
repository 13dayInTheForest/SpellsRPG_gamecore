from fastapi import APIRouter, Depends
from src.domain.users.service import UserService
from src.domain.users.schemas import *


router = APIRouter(
    prefix='/users',
    tags=['Users'])


@router.post('/')
async def create_user(user: CreateUserSchema) -> UserSchema:
    service = UserService()
    return await service.create_user(user)


@router.get('/{user_id}')
async def get_user_by_id(user_id: int) -> UserSchema:
    service = UserService()
    return await service.find_user_by_id(user_id)


@router.patch('/{user_id}')
async def update_user(user_updates: UpdateUserSchema, user_id: int) -> UserSchema:
    service = UserService()
    return await service.update_user(user_updates)


@router.delete('/{user_id}')
async def delete_user(user_id: int) -> UserSchema:
    service = UserService()
    return await service.delete_user(user_id)


@router.get('/find_by_tg/{telegram_id}')
async def find_user_by_telegram_id(telegram_id: int):
    service = UserService()
    return await service.find_user_by_telegram_id(telegram_id)

