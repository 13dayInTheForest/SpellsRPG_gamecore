from motor.motor_asyncio import AsyncIOMotorClient
from ..config import settings


client = AsyncIOMotorClient(settings.MONGO_URI)
database = client[settings.MONGO_DB_NAME]


gods_collection = database['gods']
classes_collection = database['classes']
weaknesses_collection = database['weaknesses']
potentials_collection = database['potential']

