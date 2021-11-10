import aiohttp
import requests
from steam.trade import Inventory

class client:
    def __init__(self, server_url) -> None:
        self.server_url = server_url

        self.ping()
        
    def ping(self):
        res = (requests.get(f"{self.server_url}/ping"))
        
        resp = res.json()
        if resp["success"] == True:
            print(f"ping success {resp}")

        elif res["success"] == False or res.status_code != 200:
            raise Exception(f"ping failed, code {res.status_code} json resp: {resp}")


    async def get_inv(self, steam_id:str):
        url = self.server_url  + "/load_steam_inventory"
        headers = {
            "steam_id": str(steam_id)
        }
        async with aiohttp.ClientSession() as session:
            async with session.get(url, headers=headers) as resp:
                print(f"Made Inv Request: {resp.status}")

                json_data = await resp.json()
                
                if resp.status != 200 or json_data["success"] == False:
                    print(f"inventory load failed, code {resp.status_code} json resp: {json_data}")
                    return False, f"inventory load failed, code {resp.status_code} json resp: {json_data}"



                inv = Inventory("nothing", json_data["data"], steam_id)
                return True, inv    
