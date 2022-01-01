from pydantic import BaseSettings
from functools import lru_cache

class Settings(BaseSettings):

    SENTRY_DSN: str = ...
    SENTRY_ENV: str = ...
    SENDGRID_API_KEY: str = ...
    JWT_SECRET: str = ...

    # Database
    DATABASE_NAME: str = ...
    USER_NAME: str = ...
    PASSWORD: str = ...
    HOST: str = ...
    PORT: int = ...

    class Config:
        env_file = ".env"


@lru_cache
def getEnv():
    return Settings()