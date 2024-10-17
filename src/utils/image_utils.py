import httpx


async def get_picture_from_url(url: str, bearer_token: str = None):
    async with httpx.AsyncClient() as client:
        picture = await client.get(
            url=url
        )
        return picture.content

