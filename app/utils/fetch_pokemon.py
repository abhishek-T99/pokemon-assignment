import httpx
import asyncio
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models.pokemon import Pokemon


async def fetch_pokemon_details(url: str):
    pokemon_data = []
    async with httpx.AsyncClient() as client:
        while url:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()

            tasks = [fetch_pokemon_detail(client, result['url']) for result in data['results']]
            pokemon_details = await asyncio.gather(*tasks)

            for details in pokemon_details:
                pokemon_data.append({
                    "name": details["name"],
                    "image": details["sprites"]["other"]["official-artwork"]["front_default"],
                    "types": [t["type"]["name"] for t in details["types"]],
                })

            url = data.get("next")

    return pokemon_data


async def fetch_pokemon_detail(client: httpx.AsyncClient, url: str):
    response = await client.get(url)
    response.raise_for_status()
    return response.json()


async def store_pokemon_db(db_session: AsyncSession, pokemon_list: list):
    for pokemon in pokemon_list:
        # Check if Pokemon with the same name already exists
        result = await db_session.execute(select(Pokemon).where(Pokemon.name == pokemon['name']))
        existing_pokemon = result.scalars().first()

        if not existing_pokemon:
            db_pokemon = Pokemon(name=pokemon['name'], image=pokemon['image'], types=pokemon['types'])
            db_session.add(db_pokemon)

    await db_session.commit()
