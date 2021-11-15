import websocket, json

# create on_open function that recieves a websocket connection "ws"
def on_open(ws):
  print("opened connection")
  # send message (payload) to coinbase pro that you want to subscribe to a particular symbol
  subscribe_message = {
    "type": "subscribe",
    "channels": [
      {"name": "ticker",
        "product_ids":["BTC-USD"],}
    ]
  }
  ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
  print("recieved message")
  # convert json message back to python dictionary
  print(message)
# establish socket connection to coinbase pro
socket = "wss://ws-feed.pro.coinbase.com"

# this accepts socket as the main parameter
# accepts call back functions: on_open
# when it recieves ticker data, need to process that message-> on_message=on_message
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)

# run websocket app
ws.run_forever()