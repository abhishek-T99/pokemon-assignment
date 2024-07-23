from app.core.pydantic import Schema
from typing import List, Dict

class PokemonSchema(Schema):
    id: int
    name: str
    image: str | None
    type: List[Dict]
