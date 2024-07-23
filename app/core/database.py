from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.declarative import declared_attr

class Base(DeclarativeBase):
    # generate __tablename__ automatically
    @declared_attr
    def __tablename__(cls) -> str:
        tablename = cls.__name__.lower()
        return tablename
