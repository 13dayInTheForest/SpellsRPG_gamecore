from fastapi import APIRouter
from src.application.characters.usecase import CharacterUseCase
from src.domain.characters.schemas import CreateCharacterSchema


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
    use_case = CharacterUseCase()
    return await use_case.get_character_info(telegram_id)


