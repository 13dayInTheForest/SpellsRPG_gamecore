from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv

load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='../../.env'
    )
    TOGETHER_API_KEY: str

    DEFAULT_STYLE: str
    PROFILE_STYLE_PROMPT: str
    TEMPLE_PROFILE_PROMPT: str


settings = Settings()

