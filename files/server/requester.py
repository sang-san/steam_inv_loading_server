import aiohttp


def get_inv_url(steam_id:str):
    return f"https://steamcommunity.com/inventory/{steam_id}/440/2"


async def request_inventory(steam_id:str, proxy_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(get_inv_url(steam_id), proxy=proxy_url) as resp:
            return resp.status, await resp.json()
