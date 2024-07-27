# pcost.py
#
# Exercise 1.27

import re
def portfolio_cost(filename):
    total_cost = 0.0
    with open(filename, 'rt') as f:
        next(f) #Skip headers
        for i, line in enumerate(f, start=1):
            values = line.split(',')
            if len(values) >= 3:
                if is_int(values[1]) and is_float(values[2]):
                    shares = int(values[1])
                    pricePerShare = float(values[2])
                    total_cost += shares * pricePerShare
                else:
                    print(f"Couldn't convert line# {i}: {values}")
            else:
                print(f"Couldn't convert line# {i}: {values}")
    return total_cost

def is_int(num_string):
    return re.match(r'^[+-]?\d+$', num_string) is not None

def is_float(num_string):
    return re.match(r'^[+-]?\d*\.\d+$|^[+-]?\d+\.\d*$', num_string) is not None

cost = portfolio_cost('Data/portfolio.csv')
print(f'Total cost: {cost:<10.2f}')
