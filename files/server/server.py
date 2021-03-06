from aiohttp import web
from .requester import request_inventory
from steam.trade import Inventory
import steam
import random
import time

class server:
    def __init__(self, proxys=[]) -> None:
        self.app = web.Application()

        self.proxys = proxys or None

        self.app.add_routes([
            web.get("/ping", self.ping),
            web.get("/load_steam_inventory", self.get_inv),
            web.get("/load_steam_inventory_asset_ids_only", self.get_inv_name_asset_ids_only)
        ])
    
    def get_proxy(self):
        return random.sample(self.proxys, 1)[0] if self.proxys else ""

    async def ping(self, request):
        print(f"Got pinged by {request.remote} {time.time()}")
        return web.json_response({
            "success": True,
            "time": time.time()
        })

    async def get_inv_name_asset_ids_only(self, request):
        
        if not "steam_id" in request.headers:
            return web.json_response({
                "success": False,
                "error": "did not provide a steam_id header",
                "time": time.time()
            })

        else:
            steam_id = str(request.headers["steam_id"])
            request_code, data = await request_inventory(steam_id, proxy_url=self.get_proxy())
            
            print(f"Got Name To AssetIds Request for {steam_id} by {request.remote} at {time.time()}")
            if request_code != 200:
                return web.json_response({
                    "success": False,
                    "error": f"requesting an inventory failed, {request_code} data: {data}",
                    "time": time.time()
                })

            else:
                return_data = {}

                inv = Inventory("nothing", data, steam_id, steam.TF2)
                for item in inv.items:
                    if not item.name in return_data:
                        return_data[item.name] = [str(item.asset_id)]

                    else:
                        return_data[item.name].append(str(item.asset_id))

                return web.json_response({
                    "success": True,
                    "request_status_code": request_code,
                    "data": return_data,
                    "time": time.time()
                })

    async def get_inv(self, request):
        if not "steam_id" in request.headers:
            return web.json_response({
                "success": False,
                "error": "did not provide a steam_id header",
                "time": time.time()
            })

        else:
            steam_id = str(request.headers["steam_id"])
            request_code, data = await request_inventory(steam_id, proxy_url=self.get_proxy())

            print(f"Got Inv Request for {steam_id} by {request.remote} at {time.time()}")
            return web.json_response({
                "success": True,
                "request_status_code": request_code,
                "data": data,
                "time": time.time()
            }) 

    def start(self): 
        web.run_app(self.app)


