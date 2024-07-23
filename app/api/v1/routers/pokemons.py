from app.api.v1.dependencies import SessionDep
# from app.schemas.pokemon import PokemonSchema
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1/pokemons",
    tags=["Pokemons"]
)

@router.get("/")
async def list_all_pokemons(session: SessionDep):
    pass
