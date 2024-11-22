from fastapi import HTTPException
import httpx

from src.domain.pictures.schemas import PicDetail, CreatePicRequest
from src.domain.pictures.ai_pictures import IAIPictureService
from src.infrastructure.config import settings


class FluxFreeAIPictureService(IAIPictureService):
    async def get_picture(self, pic_request: CreatePicRequest) -> PicDetail:
        try:
            async with httpx.AsyncClient() as together:
                response = await together.post(
                    timeout=10,

                    url="https://api.together.xyz/v1/images/generations",

                    headers={
                        "Authorization": f"Bearer {settings.TOGETHER_API_KEY}",
                        "Content-Type": "application/json"
                    },
                    json={
                        "model": "black-forest-labs/FLUX.1-schnell",
                        "prompt": pic_request.prompt,
                        "width": 1024,
                        "height": 1024,
                        "steps": 4,
                        "n": 1,
                        "response_format": "url",
                    }
                )
                response = response.json()

                if response.get('error'):
                    raise HTTPException(status_code=400, detail=response['error']['message'])

                return PicDetail(
                    user=pic_request.username,
                    prompt=pic_request.prompt,
                    url=response['data'][0]['url'],
                    response_time=response['data'][0]['timings']['inference']
                )
        # except httpx.TimeoutException:
        #     raise HTTPException(status_code=400, detail='Together API Read Timeout')

        except httpx.HTTPError:
            raise HTTPException(status_code=400, detail='Something went wrong with Together API')

