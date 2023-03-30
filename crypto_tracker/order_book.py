import requests
import time

# Specify the trading pair you want to track
symbol = 'BTCUSDT'

while True:
    # Retrieve the order book data from Finance
    response = requests.get(f'https://api.binance.com/api/v3/depth?symbol={symbol}&limit=10000000')
    data = response.json()

    # Calculate the total bid quantity and total ask quantity
    bids = data['bids']
    asks = data['asks']
    total_bid_quantity = sum([float(bid[1]) for bid in bids])
    total_ask_quantity = sum([float(ask[1]) for ask in asks])
    quantity_diff = total_bid_quantity - total_ask_quantity

    # Print the information
    print(f'Trading pair: {symbol}')
    print(f'Total bid quantity: {total_bid_quantity:.8f} BTC')
    print(f'Total ask quantity: {total_ask_quantity:.8f} BTC')
    print(f'Quantity difference: {quantity_diff:.8f} BTC')
    print('-' * 35)

    # Wait for 1 minutes before updating the information
    time.sleep(60)
