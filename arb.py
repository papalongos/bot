import ccxt
import config

kucoin = ccxt.kucoin()
exchange_id = 'kucoin'
exchange_class = getattr(ccxt, exchange_id)
kucoin = exchange_class({
    'rateLimit': 899,
    'enableRateLimit': True,
    'apiKey': config.KUCOIN_API_KEY,
    'secret': config.KUCOIN_SECRET_KEY,
    'password': config.KUCOIN_PASSWORD,
})

symbol = 'BTC/USDT'
base = 'BTC'
quote = 'USDT'
amount = 0.000039

# his not going to sit throug bugfixing.
# Fix yourself.
# Get to the point where he can see results (some money earned), get him excited.

order_book = kucoin.fetch_order_book(symbol)

# print(order_book)

ask = order_book['asks'][0][0]
bid = order_book['bids'][0][0]

print(f'Ask: {ask}')
print(f'Bid: {bid}')

spread = ask - bid

print(f'Spread: {spread}')

new_bid = bid + (bid * spread)
new_ask = ask - (ask * spread)

print(f'New ask: {new_ask}')
print(f'New bid: {new_bid}')

# buy_order = kucoin.create_order(symbol, 'limit', 'buy', new_ask)
# sell_order = kucoin.create_order(symbol, 'limit', 'sell', new_bid)

# print(buy_order)
# print(sell_order)
