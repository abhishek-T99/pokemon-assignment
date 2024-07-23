from typing import List,Optional
from app.models import Pokemon
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.pokemon import PokemonSchema


async def get_pokemons(
        session: AsyncSession,
        name: Optional[str] = None
) -> List[PokemonSchema]:
    query = select(Pokemon)
    if name:
        query = query.filter(Pokemon.name.ilike(f"%{name}%"))
    pokemons = (await session.scalars(query)).all()
    if not pokemons:
        raise HTTPException(status_code=404, detail="No pokemons found")
    return pokemons
