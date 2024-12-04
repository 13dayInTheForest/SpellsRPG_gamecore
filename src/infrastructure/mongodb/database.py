from motor.motor_asyncio import AsyncIOMotorClient
from ..config import settings


client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.MONGO_DB_NAME]

collections = {
    'gods': database['gods'],
    'classes': database['classes']
}


async def mongo_connect():
    try:
        await client.admin.command('ping')
    except Exception as e:
        print(f'error: {e}')
