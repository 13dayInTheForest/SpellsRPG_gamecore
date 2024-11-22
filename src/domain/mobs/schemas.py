from pydantic import BaseModel
from enum import Enum


class MobTypes(Enum):
    Monster = 'monster'
    Animal = 'animal'
    Npc = 'npc'

