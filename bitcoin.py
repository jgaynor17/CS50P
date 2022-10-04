#import btc API
#get CLI ipnut and check for place CLI[1]
#multiply and print BTC price from API by CLI[1]
#if no CLI, print Missing command-line argument and use sys.exit
#if non numerical CLI, print Command-line argument is not a number and use sys.exit
#use thousands separator

import json #improves API readibility
import sys #import system
import inflect #import inflect (to allow for comma separation as per line 6)
import requests #import requests, (allows for API importing)

p = inflect.engine()

if len(sys.argv) == 2:
    try:
        multiplier = float(sys.argv[1])
    except ValueError: #error message for argv datatype
        print("Command-line argument is not a number")
        sys.exit #quit

    try:
        data = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json") #gets the api from this URL
    except requests.RequestException:
        pass

    rate = float(data.json()["bpi"]["USD"]["rate_float"])
    amount = multiplier * rate
    print(f"${amount:,.4f}")

else:
    sys.exit("Missing command-line argument.")
