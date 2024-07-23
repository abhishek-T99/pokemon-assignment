import aiohttp
import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.pokemon import Pokemon


async def fetch_pokemon_details(url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()
            data = await response.json()

    async def fetch_details(pokemon_url: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(pokemon_url) as response:
                response.raise_for_status()
                return await response.json()

    # Create a list of tasks to fetch details for each Pokémon
    tasks = [fetch_details(result['url']) for result in data['results']]
    details = await asyncio.gather(*tasks)
    
    # Process and structure the Pokémon data
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
        # Check if Pokémon with the same name already exists
        result = await db_session.execute(select(Pokemon).where(Pokemon.name == pokemon['name']))
        existing_pokemon = result.scalars().first()

        if not existing_pokemon:
            db_pokemon = Pokemon(name=pokemon['name'], image=pokemon['image'], types=pokemon['types'])
            db_session.add(db_pokemon)

    await db_session.commit()
