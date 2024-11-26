from sqlalchemy import Table, Column, String, Integer, JSON
from src.infrastructure.python_databases.database import metadata


gods = Table(
    'gods',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('description', String),
    Column('terms', String),
    Column('picture_url', String),

    # Все значения взяты с таблицы users.
    Column('needs', JSON, default='{}'),  # Что нужно от игрока для поклонения
    Column('changes', JSON, default='{}'),   # Баффы и Нерфы для игрока
    Column('fight_changes', JSON, default='{}')   # Баффы и Нерфы для игрока во время боя
)
'''

    Пример json для needs
    {
    "needs": {
        "required_conditions": 3, ----------------------------------------------Сколько нужно выполненных условий
        "conditions": [ --------------------------------------------------------Поле Игрока, Больше/меньше/ровно, Значение
            {"field": "hp", "operator": ">", "value": 100} ---------------------В качестве операторов указываются ><=
            ]
        }
    }

    Пример json для changes
    {
    "buff": {
        "required_conditions": 3, ----------------------------------------------Сколько нужно выполненных условий
        "conditions": [ --------------------------------------------------------Перечисление условий
            {"field": "hp", "operator": ">", "value": 10}, ---------------------Поле Игрока, Больше/меньше/ровно, Значение
            {"field": "strength", "operator": ">", "value": 100} ---------------В качестве операторов указываются ><=
            ]
        "player_effects": [ ----------------------------------------------------Эффекты для игрока
            {"field": "karma", "operation": "+", "value": 50}, ----------------Поле Игрока, Добавить/отнять/перезаписать, Значение
            {"field": "mana", "operation": "-", "value": 20} -------------------В качестве операторов указываются +-r
            ]
        }
    }


    Пример json для fight_changes
    {
    "buff": {
        "required_conditions": 3, ----------------------------------------------Сколько нужно выполненных условий
        "conditions": [ --------------------------------------------------------Перечисление условий
            {"field": "hp", "operator": ">", "value": 10}, ------------------Поле Врага, Больше/меньше/ровно, Значение
            {"field": "strength", "operator": ">", "value": 100} ---------------В качестве операторов указываются ><=
            ],
        "player_effects": [ ----------------------------------------------------Эффекты для игрока
            {"field": "karma", "operation": "+", "value": 50}, ----------------Поле Игрока, Добавить/отнять/перезаписать, Значение
            {"field": "mana", "operation": "-", "value": 20} -------------------В качестве операторов указываются +-r
            ]
        }
    }
    
    
'''