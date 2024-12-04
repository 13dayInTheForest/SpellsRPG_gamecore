from .base import BaseRepo
from src.domain.gods.repository import IGodsRepo


class GodsRepo(BaseRepo, IGodsRepo):
    pass


'''
    Пример документа:
    {
    "_id": ID,
    "active": Доступен ли бог игрокам
    "name": Имя 
    "description": Описание / История
    "terms": Описание условий, т.е. что нужно для того чтобы поклоняться
    "picture_url": ссылка на картинку бога
    "needs": [
        {"field": "hp", "operator": ">", "value": 100} -------В качестве операторов указываются ><=
        {"field": "exp_points", "operator": ">", "value": 10}
    ]
    "changes": [
        {"field": "mana", "operation": "minus", "value": 10, "random": true},
        {"field": "hp", "operation": "plus", "value": 15, "depends": {"mana": 10}}
    ]
    "abilities": [id способностей которые открываются]
    }
    

'''
