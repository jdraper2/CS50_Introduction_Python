import requests
import json
import sys

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    arg_check = float(sys.argv[1])
    #print(arg_check)
except:
    sys.exit("Command-line argument is not a number")


response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
# print(json.dumps(response.json(), indent=2))

o = response.json()

current_price = float(o["bpi"]["USD"]["rate"].replace(",", "") )
total_price = current_price * float(sys.argv[1])

print(f"${total_price:,.4f}".format(total_price))
