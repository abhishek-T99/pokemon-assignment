from typing import Annotated

from app.core.database import get_db_session
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

SessionDep = Annotated[AsyncSession, Depends(get_db_session)]
