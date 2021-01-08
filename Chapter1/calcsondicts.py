'''
Problem:
perform useful calculations on default dicts:

To perform operations it is often important to invert the keys and values of the dictionary using zip().



be aware when using zip....

It creates an iterator that can only be consumed once! see below ZIP CAUTION example
'''



prices = {
'ACME': 45.23,
'AAPL': 612.78,
'IBM': 205.55,
'HPQ': 37.20,
'FB': 10.75
}


minimum_prices = min(zip(prices.values(),prices.keys()))
prices_sorted = sorted(zip(prices.values(),prices.keys()))

prices = zip(prices.values(),prices.keys())


state_ny = 8262
local_ny = 5185

state_az = 4891

savings_state = state_ny - state_az
print(savings_state + local_ny)