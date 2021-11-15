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

```python

```