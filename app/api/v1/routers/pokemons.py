from typing import Optional
from app.api.v1.dependencies import SessionDep
import app.crud.pokemon
from app.utils.fetch_pokemon import (
    fetch_pokemon_details,
    store_pokemon_db,
)
from app.schemas.pokemon import PokemonPaginatedResponseSchema
from app.core.config import config
import app.crud
from fastapi import APIRouter, Query, HTTPException


router = APIRouter()


@router.get("/", response_model=PokemonPaginatedResponseSchema)
async def list_all_pokemons(
    *,
    session: SessionDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=1500),
    name: Optional[str] = Query(None),
    type: Optional[str] = Query(None)
):
    pokemon_count = await app.crud.pokemon.get_total_pokemon_count(session=session)

    if pokemon_count == 0:
        pokemon_list = await fetch_pokemon_details(config.poke_api_url)
        await store_pokemon_db(db_session=session, pokemon_list=pokemon_list)

        pokemon_count = await app.crud.pokemon.get_total_pokemon_count(session=session)

        if pokemon_count == 0:
            raise HTTPException(
                status_code=502,
                detail="Failed to fetch data from external API."
            )

    pokemons = await app.crud.pokemon.get_pokemons(session=session, name=name, type=type)
    paginated_pokemons = pokemons[skip: skip + limit]

    return {
        "total": len(pokemons),
        "skip": skip,
        "limit": limit,
        "response": paginated_pokemons
    }
