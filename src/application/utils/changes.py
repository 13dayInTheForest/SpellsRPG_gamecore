import datetime
import random

from src.domain.characters.schemas import *


def apply_effects(character: CharacterSchema, changes: list) -> CharacterSchema:
    character = character.dict()
    if changes is not None:
        for change in changes:
            match change['operation']:

                case 'minus':

                    value = change['value'] if change.get('value') else 0
                    # Добавить зависимости если они есть в процентном соотношении
                    if change.get('depends'):
                        for field, percent in change['depends'].items():
                            value += int(character[field] / 100 * percent)
                    # Создать случайное число от 0 до значения если поле random указано
                    if change.get('random'):
                        value = random.randint(0, value)

                    # Проверка на отрицательные числа, если значение уходит в минус, заменить значение на ноль
                    # Только поле gold может уходить в минус
                    if character[change['field']] - value < 0 and change['field'] != 'gold':
                        value = character[change['field']]
                    # отнять результат value от поля
                    character[change['field']] -= value

                case 'plus':

                    value = change['value'] if change.get('value') else 0
                    # Добавить зависимости если они есть в процентном соотношении
                    if change.get('depends'):
                        for field, percent in change['depends'].items():
                            value += int(character[field] / 100 * percent)
                    # Создать случайное число от 0 до значения если поле random указано
                    if change.get('random'):
                        value = random.randint(0, value)

                    # Проверка на лимиты, если value превышает max значение, то просто заменить на максимум
                    if change['field'] == 'mana' and value + character['mana'] > character['max_mana']:
                        character[change['mana']] = character['max_mana']
                    elif change['field'] == 'hp' and value + character['hp'] > character['max_hp']:
                        character[change['hp']] = character['max_hp']
                    else:
                        # В противном случае добавить результат value к полю
                        character[change['field']] += value

                case 'multiply':

                    value = change['value'] if change.get('value') else 0
                    # Добавить зависимости если они есть в процентном соотношении
                    if change.get('depends'):
                        for field, percent in change['depends'].items():
                            value += int(character[field] / 100 * percent)
                    # Создать случайное число от 0 до значения если поле random указано
                    if change.get('random'):
                        value = random.randint(0, value)

                    # Проверка на лимиты, если value превышает max значение, то просто заменить на максимум
                    if change['field'] == 'mana' and value * character['mana'] > character['max_mana']:
                        character[change['mana']] = character['max_mana']
                    elif change['field'] == 'hp' and value * character['hp'] > character['max_hp']:
                        character[change['hp']] = character['max_hp']
                    else:
                        # В противном случае добавить результат value к полю
                        character[change['field']] *= value if value > 0 else 1

                case 'divide':

                    value = change['value'] if change.get('value') else 0
                    # Добавить зависимости если они есть в процентном соотношении
                    if change.get('depends'):
                        for field, percent in change['depends'].items():
                            value += int(character[field] / 100 * percent)
                        # Создать случайное число от 0 до значения если поле random указано
                    if change.get('random'):
                        value = random.randint(0, value)
                    # Деление без проверок потому что ниже нуля значение не сможет быть
                    character[change['field']] = int(character[change['field']] / value)

                case 'replace':
                    if change.get('depends'):
                        # Создает итератор из словаря и берет первое значение
                        field, percent = next(iter(change['depends'].items()))
                        character[change['field']] = int(character[field] / 100 * percent)
                    else:
                        character[change['field']] = change['value']

    return CharacterSchema(**character)


# char = CreateCharacterSchemaForDB(**CreateCharacterSchema(
#     telegram_user_id='123214214',
#     name='asdasd',
#     avatar_prompt='sadsad',
#     avatar_prompt_ru='sadasd',
#     avatar_url='asdasd'
# ).dict())
#
# char = CharacterSchema(id=12, born_date=datetime.now(), **char.dict())
#
# chang = [
#             {"field": "max_mana", "operation": "multiply", "value": 2},
#             {"field": "mana", "operation": "replace", "depends": {'max_mana': 100}},
#             {"field": "hp", "operation": "divide", "value": 2},
#             {"field": "hp", "operation": "minus", "value": 1000},
#             {"field": "gold", "operation": "minus", "value": 1000},
#             {"field": "strength", "operation": "multiply", "depends": {'monsters_killed': 100}}
#         ]
#
#
# char.monsters_killed = 56
# print(char.max_mana, char.mana, char.strength, char.hp)
#
#
# result = apply_effects(char, chang)
# print(result.max_mana, result.mana, result.strength, result.hp, result.gold)

