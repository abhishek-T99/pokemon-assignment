from typing import List
from app.api.v1.dependencies import SessionDep
import app.crud.pokemon
from app.utils.fetch_pokemon import fetch_pokemon_details, store_pokemon_db
from app.schemas.pokemon import PokemonSchema
import app.crud
from fastapi import APIRouter

router = APIRouter()

POKE_API_URL="https://pokeapi.co/api/v2/pokemon?limit=1500"

@router.get("/", response_model=List[PokemonSchema])
async def list_all_pokemons(*, session: SessionDep):
    pokemons = await app.crud.pokemon.get_pokemons(session=session)
    return pokemons

@router.post("/extract-and-store")
async def store_pokemon(*, session: SessionDep):
    pokemon_list = await fetch_pokemon_details(POKE_API_URL)
    await store_pokemon_db(db_session=session, pokemon_list=pokemon_list)
    return {"message": "pokemon data extracted and stored successfully"}
