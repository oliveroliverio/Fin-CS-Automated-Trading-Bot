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

want to keep track of what minutes are processed.  So create a new dictionary

```python
import websocket, json

minutes_processed = {}

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
