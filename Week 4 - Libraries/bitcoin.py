# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

import sys
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")
else:
    requests = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json", timeout=10)

    try:
        float(sys.argv[1])
    except requests.RequestException:
        sys.exit("Command-line argument is not a number")

    data = requests.json()
    current_price = data["bpi"]["USD"]["rate"]
    current_price = current_price.replace(",", "")
    price = float(sys.argv[1]) * float(current_price)
    print(f"${price:,.4f}")
