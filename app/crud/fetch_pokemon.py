import httpx
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.pokemon import Pokemon
from app.core.config import config


# async def fetch_all_pokemon():
#     url = config.poke_api_url
#     async with httpx.AsyncClient() as client:
#         response = await client.get(url)
#         response.raise_for_status()
#         data = response.json()
#     return data['results']

async def fetch_pokemon_details(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        data = response.json()
    
    async def fetch_details(pokemon_url: str):
        async with httpx.AsyncClient() as client:
            response = await client.get(pokemon_url)
            response.raise_for_status()
            return response.json()

    tasks = [fetch_details(result['url']) for result in data['results']]
    details = await asyncio.gather(*tasks)
    
    pokemon_data = []
    for i, detail in enumerate(details):
        pokemon = {
            "name": data['results'][i]['name'],
            "image": detail["sprites"]["other"]["official-artwork"]["front_default"],
            "types": [t["type"]["name"] for t in detail["types"]]
        }
        pokemon_data.append(pokemon)
    
    return pokemon_data


async def store_pokemon_db(db_session: AsyncSession, pokemon_list: list):
    for pokemon in pokemon_list:
        db_pokemon = Pokemon(name=pokemon['name'], image=pokemon['url'], types=pokemon['types'])
        db_session.add(db_pokemon)
    await db_session.commit()