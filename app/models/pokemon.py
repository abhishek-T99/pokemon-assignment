from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ARRAY
from sqlalchemy import String

from . import Base


class Pokemon(Base):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(200), unique=True, index=True)
    image: Mapped[str] = mapped_column(String(500), unique=True)
    types: Mapped[list] = mapped_column(ARRAY(String), nullable=True)
