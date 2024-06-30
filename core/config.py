import enum
import os

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load the .env file
load_dotenv(".env")


class EnvironmentType(str, enum.Enum):
    DEVELOPMENT = "development"
    PRODUCTION = "production"
    TEST = "test"


class BaseConfig(BaseSettings):
    class config:
        case_sensitive = True


class Config(BaseConfig):
    DEBUG: int = 0
    DEFAULT_LOCAL: str = "en_US"
    ENVIRONMENT: str = EnvironmentType.DEVELOPMENT
    POSTGRES_URL: str | None = os.getenv("POSTGRES_URL")
    RELEASE_VERSION: str = "0.1"
    SHOW_SQL_ALCHEMY_QUERIES: int = 0
    JWT_SECRET_KEY: str | None = os.getenv("JWT_SECRET_KEY")
    JWT_ALGORITHM: str | None = os.getenv("JWT_ALGORITHM")
    JWT_EXPIRE_MINUTES: int = 60 * 24


config: Config = Config()
