from time import perf_counter
import requests

def hello():
	a=perf_counter()

	requests.get(url="https://fapi.binance.com/fapi/v1/ticker/24hr?symbol=BNBUSDT")

	b=perf_counter()
	print(b-a)
hello()
