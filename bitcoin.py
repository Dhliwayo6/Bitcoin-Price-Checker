import sys
import requests
import json

def price_checker():

    try:

        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')

        data = response.json()

        bitcoin_price = (data['bpi']['USD']['rate'])

        print(bitcoin_price)

        bitcoin_price = bitcoin_price.replace(',', '')

        num_of_coins = sys.argv[1]

        if float(num_of_coins):
            price = float(num_of_coins) * float(bitcoin_price)
        
        
        return f"${price:,.4f}" # comma is a thousands separator

    except ValueError:
        sys.exit('Command-line argument is not a number')

    except requests.RequestException:
        sys.exit()

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')

    print(price_checker())
