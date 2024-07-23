from typing import List
from app.api.v1.dependencies import SessionDep
import app.crud.pokemon
import app.utils.fetch_pokemon
from app.schemas.pokemon import PokemonSchema
import app.crud
from app.core.config import config
from fastapi import APIRouter

router = APIRouter()

@router.get("/", response_model=List[PokemonSchema])
async def list_all_pokemons(*, session: SessionDep):
    pokemons = await app.crud.pokemon.get_pokemons(session=session)
    return pokemons

@router.post("/extract-and-store")
async def store_pokemon(*, session: SessionDep):
    pokemon_list = await app.utils.fetch_pokemon.fetch_pokemon_details(config.poke_api_url)
    await app.utils.fetch_pokemon.store_pokemon_db(db_session=session, pokemon_list=pokemon_list)
    return {"message": "pokemon data extracted and stored successfully"}
