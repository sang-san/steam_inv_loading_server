from files.server.server import server



# list of http proxy urls
proxys = []

server(proxys=proxys).start()