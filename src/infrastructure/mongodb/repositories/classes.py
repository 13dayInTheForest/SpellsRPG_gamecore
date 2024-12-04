from .base import BaseRepo
from src.domain.classes.repository import IClassesRepo


class ClassesRepo(BaseRepo, IClassesRepo):
    pass


'''
{
    "id": int,
    "name": str,
    "description": str,
    "terms": Optional[str],
    "picture_url": Optional[str],
    "needs": [ 
        {"field": "hp", "operator": ">", "value": 100},
        {"field": "human_killed", "operator": ">", "value": 99}
    ],
    "changes": [
        {"field": "mana", "operation": "minus", "value": 10},
        {"field": "hp", "operation": "plus", "value": 15, "depends": {"mana": 10}}
    ],
}

'''
