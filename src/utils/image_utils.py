import httpx
from fastapi import HTTPException


async def get_picture_from_url(url: str):
    async with httpx.AsyncClient() as client:
        picture = await client.get(
            url=url
        )
        if picture.status_code != 200:
            raise HTTPException(status_code=picture.status_code, detail='cant find picture')
        return picture.content


