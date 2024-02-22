from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    secret_key: str = Field(default="", description="secret_key")
    algorithm: str = Field(
        default="", description="chosen algorithm for jwt encryption"
    )
    access_token_expires_minutes: int = Field(
        default=30, description="token expiration time in minutes"
    )
    database_url: str = Field(default="", description="database url")

    model_config = SettingsConfigDict(env_file=".env")
