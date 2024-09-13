import requests
import csv
from datetime import datetime, timedelta
import argparse
import re

def extract_pool_id(url):
    match = re.search(r'/pools/([^/]+)$', url)
    return match.group(1) if match else None

def get_pool_info(network, pool_id):
    base_url = f"https://api.geckoterminal.com/api/v2/networks/{network}/pools/{pool_id}"
    response = requests.get(base_url)
    if response.status_code == 200:
        data = response.json()
        return data['data']['attributes']
    else:
        print(f"Error fetching pool info: {response.status_code}")
        return None

def get_token_prices(network, pool_id, start_date, end_date):
    base_url = f"https://api.geckoterminal.com/api/v2/networks/{network}/pools/{pool_id}/ohlcv/day"
    prices = []
    
    days_difference = (end_date - start_date).days + 1
    
    params = {
        'aggregate': 1,
        'before_timestamp': int(end_date.timestamp()),
        'limit': days_difference
    }
    
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        ohlcv_list = data['data']['attributes']['ohlcv_list']
        for item in ohlcv_list:
            date = datetime.fromtimestamp(item[0])
            close_price = item[4]  # Close price
            prices.append((date.strftime('%Y-%m-%d'), close_price))
    else:
        print(f"Error: {response.status_code}")
    
    return sorted(prices, key=lambda x: x[0])  # Sort by date

def sanitize_filename(name):
    # Replace '/' with '-', remove any other non-alphanumeric characters (except '-'), and replace multiple '-' with single '-'
    sanitized = re.sub(r'[/]', '-', name)
    sanitized = re.sub(r'[^\w-]', '', sanitized)
    sanitized = re.sub(r'-+', '-', sanitized)
    return sanitized.strip('-')  # Remove leading/trailing '-'

def main():
    parser = argparse.ArgumentParser(description="Fetch token prices from GeckoTerminal")
    parser.add_argument("url", help="GeckoTerminal pool URL")
    args = parser.parse_args()

    pool_id = extract_pool_id(args.url)
    if not pool_id:
        print("Invalid URL. Please provide a valid GeckoTerminal pool URL.")
        return

    network = args.url.split("/")[-3]  # Extract network from URL

    pool_info = get_pool_info(network, pool_id)
    if not pool_info:
        return

    print("Pool Info:")
    for key, value in pool_info.items():
        print(f"{key}: {value}")

    token_name = pool_info.get('name', 'Unknown')
    token_symbol = pool_info.get('symbol', token_name.split('/')[0].strip() if '/' in token_name else token_name)
    token_address = pool_info.get('address', 'Unknown')
    coingecko_id = pool_info.get('coingecko_coin_id', 'Unknown')

    print(f"\nToken Name: {token_name}")
    print(f"Token Symbol: {token_symbol}")
    print(f"Token Address: {token_address}")
    print(f"CoinGecko ID: {coingecko_id}")

    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)  # Last 6 months

    prices = get_token_prices(network, pool_id, start_date, end_date)

    csv_filename = f"{sanitize_filename(token_name)}.csv"
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Price (in USD)"])
        writer.writerows(prices)

    print(f"\nSaved {len(prices)} days of price data to {csv_filename}")
    print(f"Data range: {prices[0][0]} to {prices[-1][0]}")

if __name__ == "__main__":
    main()
