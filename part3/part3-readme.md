# Copied bot.py from part2

```python
import websocket, json

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
  print("recieved message")
  print(message)
socket = "wss://ws-feed.pro.coinbase.com"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()
```

want to keep track of what minutes are processed.  So create a new dictionary.  If minute isn't in the minute processed dictionary, create a new minute record.  We'll start with empty list of minute_candlesticks.

```python
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
  print("recieved message")
  print(message)
socket = "wss://ws-feed.pro.coinbase.com"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()
```
