import requests

# Define your portfolio with cryptocurrencies and quantities
portfolio = {
    'BTC': 2.5,
    'ETH': 5.0,
    'LTC': 10.0
}

# Function to fetch the latest prices of cryptocurrencies from the API
def fetch_crypto_prices():
    try:
        url = 'https://api.coincap.io/v2/assets'
        params = {'ids': ','.join(portfolio.keys())}
        response = requests.get(url, params=params)
        data = response.json()
        prices = {crypto['symbol']: float(crypto['priceUsd']) for crypto in data['data']}
        return prices
    except Exception as e:
        print('Error fetching cryptocurrency prices:', str(e))

# Function to calculate the current value of each cryptocurrency and the total portfolio value
def calculate_portfolio_value():
    prices = fetch_crypto_prices()

    if prices:
        total_value = 0

        for crypto, quantity in portfolio.items():
            if crypto in prices:
                price = prices[crypto]
                value = price * quantity
                total_value += value

                print(f'{crypto}:')
                print(f'Current Price: ${price:.2f}')
                print(f'Quantity: {quantity}')
                print(f'Value: ${value:.2f}')
                print('------------------')

        print(f'Total Portfolio Value: ${total_value:.2f}')

# Calculate and display the current portfolio value
calculate_portfolio_value()
