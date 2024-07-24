from typing import List,Optional
from app.models import Pokemon
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.pokemon import PokemonSchema


async def get_pokemons(
        session: AsyncSession,
        name: Optional[str] = None,
        type: Optional[str] = None,
) -> List[PokemonSchema]:
    query = select(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))

    if type:
        query = query.filter(Pokemon.types.any(type))

    pokemons = (await session.scalars(query)).all()
    return pokemons


async def get_total_pokemon_count(
        session: AsyncSession
) -> int:
    count = (await session.scalars(select(Pokemon))).all()
    return len(count)
