# Build Trading Bot.  Coinbase pro API
- Build websocket app that connects to coinbase pro
- Retrieve real time BTCUSD ticker data
- Convert to candlesticks
- Detect patterns
- Determine trading strategy with optimal risk/reward ratio

## [Websocket feed doc](https://docs.cloud.coinbase.com/exchange/docs/overview)

# install python websocket client
```
pip install websocket-client
```

# create bot.py

```
import websocket, json
```

[API doc](https://docs.cloud.coinbase.com/exchange/docs#websocket-feed)

Get address:  wss://ws-feed.pro.coinbase.com


Want to establish connect to websocket
```python
# establish socket connection to coinbase pro
socket = "wss://ws-feed.pro.coinbase.com"

# this accepts socket as the main parameter
# accepts call back functions: on_open
ws = websocket.WebSocketApp(socket)
```

Call back functions: on_message: get messages for ticker data

Subscribing to a particular ticker:

```JSON
// Request
// Subscribe to ETH-USD and ETH-EUR with the level2, heartbeat and ticker channels,
// plus receive the ticker entries for ETH-BTC and ETH-USD
{
    "type": "subscribe",
    "product_ids": [
        "ETH-USD",
        "ETH-EUR"
    ],
    "channels": [
        "level2",
        "heartbeat",
        {
            "name": "ticker",
            "product_ids": [
                "ETH-BTC",
                "ETH-USD"
            ]
        }
    ]
}
```
Add the above to the on_open() function

Added test.py for troubleshooting.  [Source](https://www.youtube.com/watch?v=ToB8-mEX8l8)

```python
import websocket, json

def on_open(ws):
  print('socket is opened')
  subscribe_message = {
    'type': 'subscribe',
    'channels': [
      {'name':'ticker',
      'product_ids':['BTC-USD']}
    ]
  }
  ws.send(json.dumps(subscribe_message))

def on_message(ws, message):
  print('getting message')
  print(message)

socket = 'wss://ws-feed.pro.coinbase.com'
ws = websocket.WebSocketApp(socket, on_open=on_open, on_message=on_message)
ws.run_forever()
```

This works.

Now trying bot.py

```python
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
```

Analyze output
```
{"type":"ticker","sequence":31107847666,"product_id":"BTC-USD","price":"63656.98","open_24h":"65505.03","volume_24h":"10230.56838838","low_24h":"63371","high_24h":"66339.9","volume_30d":"382751.40513178","best_bid":"63656.97","best_ask":"63670.59","side":"sell","time":"2021-11-15T23:29:33.529441Z","trade_id":236402106,"last_size":"0.24766071"}
recieved message

{"type":"ticker","sequence":31107847668,"product_id":"BTC-USD","price":"63656.97","open_24h":"65505.03","volume_24h":"10230.76778877","low_24h":"63371","high_24h":"66339.9","volume_30d":"382751.60453217","best_bid":"63656.96","best_ask":"63670.59","side":"sell","time":"2021-11-15T23:29:33.529441Z","trade_id":236402107,"last_size":"0.19940039"}
```

# Part 02 Conclusion
20211115 3:33pm Finished
Next we'll collect these prices, keep track of the high/low for a particular time period.  Say we got 100 of these within a minute, keep track of the OHLC within that minute up until a new minute starts.  Keep track of these candlesticks in a list, then process the end of the list to detect partciular patterns.  So next we'll process this "tick" data