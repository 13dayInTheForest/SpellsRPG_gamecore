from src.domain.characters.schemas import CharacterSchema


async def check_needs(character: CharacterSchema, needs: list, needs_count: int) -> bool:
    character = character.dict()
    if needs_count == 0:
        return True

    completed = 0
    # Открывает требования, их может быть несколько
    for requirement in needs:
        match requirement['operator']:
            case '>':
                if character[requirement['field']] > requirement["value"]:
                    completed += 1
            case '<':
                if character[requirement['field']] < requirement["value"]:
                    completed += 1
            case '=':
                if character[requirement['field']] == requirement["value"]:
                    completed += 1

    # возвращает bool
    return completed >= needs_count
