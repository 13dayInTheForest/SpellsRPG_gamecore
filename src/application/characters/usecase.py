from src.domain.characters.schemas import CreateCharacterSchema


class CharacterUseCase:
    def __init__(self,
                 user_service,
                 characters_service,
                 gods_service,
                 weaknesses_service,
                 potential_service,
                 buffs
                 ):
        self.user_interface = user_service
        self.characters_interface = characters_service

    async def create_character(self, character: CreateCharacterSchema):
        pass

    async def get_profile_stats(self):
        pass

    async def get_public_profile_stats(self):
        pass
