from typing import List
from app.api.v1.dependencies import SessionDep
import app.crud.pokemon
from app.schemas.pokemon import PokemonSchema
import app.crud
from fastapi import APIRouter

router = APIRouter()

@router.get("/", response_model=List[PokemonSchema])
async def list_all_pokemons(*, session: SessionDep):
    pokemons = await app.crud.pokemon.get_pokemons(session=session)
    return pokemons
