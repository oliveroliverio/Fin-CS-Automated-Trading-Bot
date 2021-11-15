import websocket, json



# establish socket connection to coinbase pro
socket = "wss://ws-feed.pro.coinbase.com"

# this accepts socket as the main parameter
# accepts call back functions: on_open
ws = websocket.WebSocketApp(socket, on_message=on_message)