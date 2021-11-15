import websocket, json

minutes_processed = {}
minute_candlesticks = []
current_tick = None
# store previous tick as the close of the last candle
previous_tick = None

def on_open(ws):
  print("opened connection")
  subscribe_message = {
    "type": "subscribe",
    "channels": [
      {"name": "ticker",
        "product_ids":["BTC-USD"],}
    ]
  }
  ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
  global current_tick, previous_tick
  # when you see a message
  previous_tick = current_tick
  current_tick = json.loads(message)

  # print debugging info
  print("=== Recieved Tick ===")
  # print formatted string of the timestamp and price
  print("{} @ {}".format(current_tick['time'], current_tick['price']))

socket = "wss://ws-feed.pro.coinbase.com"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()