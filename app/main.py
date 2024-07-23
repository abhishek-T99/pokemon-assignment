import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.database import sessionmanager
from app.api.v1.main import api_router

from app.core.config import config

logger = logging.getLogger("uvicorn")


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()


app = FastAPI(lifespan=lifespan, title=config.project_name, docs_url="/api/v1/docs")


# Routers
app.include_router(api_router)
