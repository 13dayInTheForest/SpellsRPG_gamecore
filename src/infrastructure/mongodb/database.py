from motor.motor_asyncio import AsyncIOMotorClient
from ..config import settings


client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.MONGO_DB_NAME]

collections = {
    'gods': database['gods'],
    'classes': database['classes'],
    'weaknesses': database['weaknesses'],
    'potentials': database['potential']
}

