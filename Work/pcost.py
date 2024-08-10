#!/usr/bin/env python
# pcost.py
#
# Exercise 1.27

import re
import sys
# import csv
import report
def portfolio_cost(filename):
    total_cost = 0.0
    # with open(filename, 'rt') as f:
        # rows = csv.reader(f)
        # headers = next(rows)
        # for rowno, row in enumerate(rows, start = 1):
            # record = dict(zip(headers, row))
            # try:
                # nshares = int(record['shares'])
                # price = float(record['price'])
                # total_cost += nshares * price
            # except ValueError:
                # print(f'Row {rowno}: Bad row: {row}')
    portfolio = report.read_portfolio(filename)
    for record in portfolio:
        nshares = record.shares
        price = record.price
        total_cost += nshares * price
    return total_cost

def is_int(num_string):
    return re.match(r'^[+-]?\d+$', num_string) is not None

def is_float(num_string):
    return re.match(r'^[+-]?\d*\.\d+$|^[+-]?\d+\.\d*$', num_string) is not None

def main(argv):
    if len(argv) < 2:
        raise SystemExit(f'Usage {argv[0]} portfile')
    fname_portfile = argv[1]
    cost = portfolio_cost(fname_portfile)
    print(f'Total cost: {cost:<10.2f}')

if __name__ == '__main__':
    main(sys.argv)

