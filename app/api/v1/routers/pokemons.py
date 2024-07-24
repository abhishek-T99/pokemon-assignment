from typing import Optional
from app.api.v1.dependencies import SessionDep
import app.crud.pokemon
from app.utils.fetch_pokemon import fetch_pokemon_details, store_pokemon_db
from app.schemas.pokemon import PokemonPaginatedResponseSchema
from app.core.config import config
import app.crud
from fastapi import APIRouter, Query


router = APIRouter()


@router.get("/", response_model=PokemonPaginatedResponseSchema)
async def list_all_pokemons(
    *,
    session: SessionDep,
    skip: int = Query(0, ge=0),
    limit: int = Query(10, le=2000),
    name: Optional[str] = Query(None),
    type: Optional[str] = Query(None)
):
    pokemons = await app.crud.pokemon.get_pokemons(session=session, name=name, type=type)

    if not pokemons:
        pokemon_list = await fetch_pokemon_details(config.poke_api_url)
        await store_pokemon_db(db_session=session, pokemon_list=pokemon_list)
        pokemons = await app.crud.pokemon.get_pokemons(session=session, name=name, type=type)

    paginated_pokemons = pokemons[skip: skip + limit]

    return {
        "total": len(pokemons),
        "skip": skip,
        "limit": limit,
        "response": paginated_pokemons
    }

