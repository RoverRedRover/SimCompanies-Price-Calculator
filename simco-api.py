#! usr/bin/python3
""" Obtain up-to-date SimCompanies Exchange price data every 15 mins.
"""

from requests import get
from json import loads
from time import sleep, ctime

# CONSTANTS

BASE_URL = 'https://www.simcompanies.com/'
API_URL = 'api/v1/market-ticker/2020-05-11T04:05:52.191Z'
READ_URL = BASE_URL + API_URL
MY_PRODUCTS = {
    2: "water",
    3: "apples",
    4: "oranges",
    5: "grapes",
    6: "grain",
    13: "transport",
    29: "plant research",
    40: "cotton",
    66: "seeds",
    72: "sugarcane",
    106: "wood"
}
MY_RESULTS = {}
PAUSE_TIME = 5  # minutes

# FUNCTIONS


def pull_data():

	response = get(READ_URL)
	#print(f'requests status code: {response.status_code}')

	market_state = loads(response.content)

	#print(market_state[0])

	for entry in market_state:

		for product in MY_PRODUCTS.values():

			if product in entry['image']:

				MY_RESULTS[product] = entry['price']

	return MY_RESULTS


# ACTIONS

for i in range(0, 4):  # run for one hour for now

	MY_RESULTS = pull_data()

	print(f'Exchange prices at {ctime()}')

	for k, v in MY_RESULTS.items():

            print(f'{k}:\t\t${v:,.3f}')

	sleep(PAUSE_TIME * 60)
	print()
