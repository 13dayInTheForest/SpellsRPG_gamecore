import requests
from PIL import Image
from together import AsyncTogether

from src.external_services.interfaces.pictures import IAIPictureService
from src.core.config import settings


client = AsyncTogether(api_key=settings.TOGETHER_API_KEY)


class FluxFreeService(IAIPictureService):
    async def get_picture(self, prompt: str) -> str:
        response = await client.images.generate(
            prompt=prompt,
            model="black-forest-labs/FLUX.1-schnell-Free",
            width=1024,
            height=768,
            steps=4,
            n=1,
        )
        return response.data[0].url


