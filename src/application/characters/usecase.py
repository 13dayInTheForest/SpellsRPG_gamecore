


class CharacterUseCase:
    def __init__(self,
                 user_interface,
                 characters_interface
                 ):
        self.user_interface = user_interface
        self.characters_interface = characters_interface

    async def create_character(self, character: ):