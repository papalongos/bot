import json
import ccxt

#print(ccxt.exchanges)

kucoin = ccxt.kucoin()
markets = kucoin.load_markets()

order_book_symbol = kucoin.symbols[0]

order_book = kucoin.fetch_order_book(kucoin.symbols[0])

print(json.dumps(order_book, indent=2))

# print(order_book)
# print(kucoin.fetch_order_book())
