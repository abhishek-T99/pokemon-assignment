from typing import List
from app.models import Pokemon
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.pokemon import PokemonSchema


async def get_pokemons(session: AsyncSession) -> List[PokemonSchema]:
    pokemons = (await session.scalars(select(Pokemon))).all()
    if not pokemons:
        raise HTTPException(status_code=404, detail="No pokemons found")
    return pokemons
