from fastapi import APIRouter, Depends
from src.domain.effects.service import EffectService
from src.domain.effects.schemas import *


router = APIRouter(
    prefix='/effects',
    tags=['Effects']
)


@router.post('/create')
async def create_effect(effect: CreateEffectSchema) -> EffectSchema:
    service = EffectService()
    return await service.create(effect)


@router.get('/get/{effect_id}')
async def get_god_by_id(effect_id: str) -> EffectSchema:
    service = EffectService()
    return await service.read(effect_id)


@router.get('/get_one')
async def get_one_by_fields(fields: EffectsQueryFilters = Depends()) -> EffectSchema:
    service = EffectService()
    return await service.read_one_by_fields(fields)


@router.get('/list')
async def get_many_by_fields(limit: int | None = 5, fields: EffectsQueryFilters = Depends()) -> dict:
    service = EffectService()
    return await service.read_many_by_fields(fields, limit)


@router.patch('/update/{effect_id}')
async def update_god(effect_id: str, updates: UpdateEffectSchema) -> EffectSchema:
    service = EffectService()
    return await service.update(effect_id, updates)


@router.delete('/delete/{effect_id}')
async def delete_god(effect_id: str) -> EffectSchema:
    service = EffectService()
    return await service.delete(effect_id)



