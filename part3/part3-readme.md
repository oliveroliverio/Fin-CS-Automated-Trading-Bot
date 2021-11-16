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

want to keep track of what minutes are processed.
So create a new dictionary.
If minute isn't in the minute processed dictionary, create a new minute record.
We'll start with empty list of minute_candlesticks.

Now add code on on_message() function to update candlestick data based on the prices that come in
- create a global current_tick and previous_tick to police into scope
-
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
  global current_tick, previous_tick
  # when you see a message
  previous_tick = current_tick
  current_tick = json.loads(message)

  # print debugging info
  print("=== Recieved Tick ===")
  # print formatted string of the timestamp and price
  print("{} @ {}", format(current_tick['time'], current_tick['price']))

socket = "wss://ws-feed.pro.coinbase.com"
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()
```
Run this: `python bot.py`

Output
```
2021-11-15T23:57:55.848199Z @ 63653.8
=== Recieved Tick ===
2021-11-15T23:57:55.904106Z @ 63651.23
=== Recieved Tick ===
2021-11-15T23:57:55.904106Z @ 63651.23
=== Recieved Tick ===
2021-11-15T23:57:55.917575Z @ 63651.23
=== Recieved Tick ===
2021-11-15T23:57:55.917575Z @ 63650
=== Recieved Tick ===
2021-11-15T23:57:56.456059Z @ 63641.66
=== Recieved Tick ===
2021-11-15T23:57:56.591046Z @ 63641.66
```

Now we can build minute candlesticks based on this tick data