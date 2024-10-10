from fastapi import HTTPException
from together import AsyncTogether

from src.external_services.interfaces.pictures import IAIPictureManager
from src.core.config import settings


client = AsyncTogether(api_key=settings.TOGETHER_API_KEY, timeout=10)


class FluxFreeAIPictureManager(IAIPictureManager):
    async def get_picture(self, prompt: str) -> str:
        try:
            response = await client.images.generate(
                prompt=prompt,
                model="black-forest-labs/FLUX.1-schnell-Free",
                width=1024,
                height=768,
                steps=4,
                n=1,
            )
            return response.data[0].url

        except Exception as e:
            raise HTTPException(status_code=400, detail=e)

