from fastapi import APIRouter
from src.application.characters.usecase import CharacterUseCase
from src.domain.characters.service import CharacterService
from src.domain.characters.schemas import *


router = APIRouter(
    prefix='/character',
    tags=['Character']
)


@router.post('/create')
async def create_character(info: CreateCharacterSchema):
    use_case = CharacterUseCase()
    return await use_case.create_character(info)


@router.get('/get/{telegram_id}')
async def get_all_character_info(telegram_id: str):
    service = CharacterService()
    return await service.find_character_by_telegram_id(telegram_id)


@router.get('/get_for_fight/{telegram_id}')
async def get_boosted_info(telegram_id: str):
    use_case = CharacterUseCase()
    return await use_case.get_character_info_for_fight(telegram_id)


@router.patch('/update/{telegram_id}')
async def update_character(telegram_id: str, updates: UpdateCharacterSchema):
    service = CharacterService()
    character = await service.find_character_by_telegram_id(telegram_id)
    return await service.update_character(character.id, updates)


@router.delete('/die/{telegram_id}')
async def character_death_process(telegram_id: str):
    pass


