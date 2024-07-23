from fastapi import APIRouter

from app.api.v1.routers import pokemons

api_router = APIRouter()
api_router.include_router(pokemons.router, prefix="/api/v1/pokemons" ,tags=["Pokemon"])