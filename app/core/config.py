import logging
from pydantic_settings import BaseSettings
from pydantic import AnyUrl
from functools import lru_cache
from pathlib import Path

BASE_DIR = Path(__file__).parent

log = logging.getLogger("uvicorn")


class Config(BaseSettings):
    database_url: AnyUrl | str
    project_name: str
    echo_sql: bool = False

    class Config:
        env_file = ".env"


@lru_cache()
def get_config() -> Config:
    log.info("Loading config settings from the environment...")
    return Config()


config = get_config()