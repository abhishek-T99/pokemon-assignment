from app.core.pydantic import Schema

class PokemonSchema(Schema):
    id: int
    name: str
    image: str | None
    types: list
