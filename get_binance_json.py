from binance.client import Client
import json
import sys

if len(sys.argv) < 3:
    print('need api key and secret key')
    sys.exit(1)

api_key = sys.argv[1]
secret_key = sys.argv[2]

pairs = ['ETHBTC','ADABTC','AVAXBTC','DOTBTC','LTCBTC','LUNABNB','SOLBNB','BAKEBNB','BTCBUSD','SOLUSDT', 'FILUPUSDT']
limits = [250, 500, 1000, 2500, 5000]

client = Client(api_key, secret_key)

filenames = 'exchange_info.json\n'

#get exchange info
data = client.get_exchange_info()
json.dump(data, open('data/exchange_info.json', 'w'), indent=4, ensure_ascii=False)


for pair in pairs:
    for limit in limits:
        data = client.get_order_book(symbol=pair, limit=250)
        filename = 'orderBook_%s_limit_%s.json' % (pair, limit)
        filenames += filename + '\n'
        json.dump(data, open('data/' + filename, 'w'), indent=4, ensure_ascii=False)

    data = client.get_recent_trades(symbol=pair, limit=1000)
    filename = 'recent_trades_%s_limit_1000.json' % pair
    filenames += filename + '\n'
    json.dump(data, open('data/' + filename, 'w'), indent=4, ensure_ascii=False)

    data = client.get_avg_price(symbol=pair)
    filename = 'average_price_%s.json' % pair
    filenames += filename + '\n'
    json.dump(data, open('data/' + filename, 'w'), indent=4, ensure_ascii=False)

print(filenames, file=open("data/data.txt", 'w'))
print('DONE!')