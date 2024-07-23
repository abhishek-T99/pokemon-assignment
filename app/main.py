import logging
from fastapi import FastAPI

from app.core.config import config

logger = logging.getLogger("uvicorn")

app = FastAPI(title=config.project_name)