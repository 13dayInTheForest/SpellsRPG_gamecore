from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../../.env'
    )
    DB_HOST: str
    DB_PORT: int
    DB_NAME: str
    DB_USER: str
    DB_PASS: str

    TOGETHER_API_KEY: str

    DEFAULT_STYLE_PROMPT: str
    PROFILE_STYLE_PROMPT: str
    TEMPLE_PROFILE_PROMPT: str

    @property
    async def get_db_url(self):
        return f'postgres+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}'


settings = Settings()

