import datetime
import random

from src.domain.characters.schemas import CharacterSchema, CreateCharacterSchema, CreateCharacterSchemaForDB


def apply_effects(character: CharacterSchema, changes: list):
    character = character.dict()
    if changes is not None:
        for change in changes:
            match change['operation']:

                case 'minus':

                    value = change['value']
                    if change.get('depends'):
                        for field, percent in change['depends'].items():
                            value += character[field] // 100 * percent
                    if change.get('random'):
                        value = random.randint(0, value)
                    character[change['field']] -= value

                case 'plus':

                    value = change['value']
                    if change.get('depends'):
                        for field, percent in change['depends'].items():
                            value += character[field] // 100 * percent
                    if change.get('random'):
                        value = random.randint(0, value)
                    character[change['field']] += value

                case 'replace':
                    if change.get('depends'):
                        for field, percent in change['depends'].items():
                            character[change['field']] = character[field] // 100 * percent
                    else:
                        character[change['field']] = change['value']

    return CharacterSchema(**character)


char = CreateCharacterSchemaForDB(**CreateCharacterSchema(
    telegram_user_id='123214214',
    name='asdasd',
    avatar_prompt='sadsad',
    avatar_prompt_ru='sadasd',
    avatar_url='asdasd'
).dict())

char = CharacterSchema(id=12, born_date=datetime.datetime.now(), **char.dict())

chang = [
            {"field": "max_mana", "operation": "plus", "value": 50},
            {"field": "mana", "operation": "replace", "depends": {'max_mana': 1000}},
            {"field": "name", "operation": "replace", "value": "РАБ"}
        ]

result = apply_effects(char, chang)
print(result.max_mana, result.mana, result.name)
