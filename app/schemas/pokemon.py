from typing import List
from app.core.pydantic import Schema
from pydantic import BaseModel

class PokemonSchema(Schema):
    id: int
    name: str
    image: str | None
    types: list


class PokemonPaginatedResponseSchema(BaseModel):
    total: int
    skip: int
    limit: int
    data: List[PokemonSchema]
