import json
from decimal import Decimal
import ccxt
from config import Config

cfg = Config('config.cfg')

kucoin = ccxt.kucoin({
    'apiKey': cfg['kucoin.api_key'],
    'secret': cfg['kucoin.secret_key'],
    'password': cfg['kucoin.api_passphrase'],
})

symbol = 'BTC/USDT'
amount = 0.000039
price = 1


# If limit=20 specified then the faster https://docs.kucoin.com/#get-part-order-book-aggregated
# endpoint will be used.
order_book = kucoin.fetch_order_book(symbol, limit=20)
# Here is the structure of the order_book object returned
# {
#   'bids': [
#     [ price, amount ], // [ float, float ]
#     [ price, amount ],
#     ...
#   ],
#   'asks': [
#     [ price, amount ],
#     [ price, amount ],
#     ...
#   ],
#   'symbol': 'ETH/BTC', // a unified market symbol
#   'timestamp': 1499280391811, // Unix Timestamp in milliseconds (seconds * 1000)
#   'datetime': '2017-07-05T18:47:14.692Z', // ISO8601 datetime string with milliseconds
#   'nonce': 1499280391811, // an increasing unique identifier of the orderbook snapshot
# }
#
# Bids: Sort price from high to low
# Asks: Sort price from low to high
#
# https://docs.ccxt.com/en/latest/manual.html#order-book-structure

# Uncomment the line below to print the order book
# print(json.dumps(order_book))

# Get the highest bid
highest_bid = order_book['bids'][0]
print(f'Highest bid: {highest_bid}')
highest_bid_price = Decimal(str(highest_bid[0]))
highest_bid_amount = Decimal(str(highest_bid[1]))
print(f'Highest bid; price: {highest_bid_price}, amount: {highest_bid_amount}')

# Get the lowest ask
lowest_ask = order_book['asks'][0]
print(f'Lowest ask: {lowest_ask}')
lowest_ask_price = Decimal(str(lowest_ask[0]))
lowest_ask_amount = Decimal(str(lowest_ask[1]))
print(f'Lowest ask; price: {lowest_ask_price}, amount: {lowest_ask_amount}')

# Calculate spread (difference)
spread = lowest_ask_price - highest_bid_price
print(f'Spread: {spread}')

# Calculate new bid price
new_bid_price = highest_bid_price + (highest_bid_price * spread)
print(f'New bid; price: {new_bid_price}')

# Calculate new ask price
new_ask_price = lowest_ask_price - (lowest_ask_price * spread)
print(f'New ask; price: {new_ask_price}')

# buy_order = kucoin.create_order(symbol, type='limit', side='buy', amount=amount, price=float(new_ask_price))
# sell_order = kucoin.create_order(symbol, type='limit', side='sell', amount=amount, price=float(new_bid_price))

# print(buy_order)
# print(sell_order)
