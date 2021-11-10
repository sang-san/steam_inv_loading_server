# steam_inv_loading_server
 Load all your Steam Inventorys remotely.
 Made this for a project, not sure if anyone needs it but here ya go.
 
# Use Case
 You have a project that loads a lot of steam tf2 inventorys and you constantly have to wait for api calls that slow down your entire project ? 
 Worry no longer, this is a simple server / client package that can run an api that then can be consumed by the client to load inventorys.
 
 When you request an inventory with a steam_id_64 you will get back an steam.py inventory. ( matching the inventory you would get from a normal steam.py .inventory() call).
 
 Only thing that is not matching is the owner attribute of the inv since the user data is not loaded to speed up the package.
 
 
 If you want to use it go ahead :)
