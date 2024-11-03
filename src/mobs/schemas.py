from pydantic import BaseModel
from enum import Enum


class MobTypes(Enum):
    Monsters = 'monsters'
    Animal = 'animal'
    Npc = 'npc'

