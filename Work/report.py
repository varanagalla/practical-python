# report.py
#
# Exercise 2.4

import csv
import locale

def read_portfolio(filename):
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        next(rows) # Ignore headers.
        for row in rows:
            portfolio.append({'name': row[0], 'shares': int(row[1]), 'price': float(row[2])})
    return portfolio
        

def read_prices(filename):
    prices = {}
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        for row in rows:
            if len(row) >= 2:
                prices[row[0]] = float(row[1])
    return prices

def make_report(portfolio, prices):
    report = []
    for pe in portfolio:
        report.append((pe['name'], pe['shares'], prices[pe['name']], prices[pe['name']] - pe['price']))
    return report


def print_report(headers):
    portfolio = read_portfolio('Data/portfolio.csv')
    prices = read_prices('Data/prices.csv')
    report = make_report(portfolio, prices)
    print('%10s %10s %10s %10s' % headers)
    print(f"{'-'*10} " * len(headers))
    locale.setlocale(locale.LC_ALL, '') # currency printing
    for name, shares, price, change in report:
        print(f'{name:>10s} {shares:>10d} {locale.currency(price):>10s} {change:>10.2f}')

headers = ('Name', 'Shares', 'Price', 'Change')
print_report(headers)

# 
# portfolio_value = 0.0
# 
# for pe in portfolio:
    # stock = pe['name']
    # nshares = pe['shares']
    # cost = pe['price']
    # price = current_prices[stock]
    # gain_or_loss = price - cost
    # portfolio_stock_value = nshares * gain_or_loss
    # portfolio_value += portfolio_stock_value
    # print(f'{stock}, {portfolio_stock_value}')
    # 
# if portfolio_value > 0:
    # print(f'You can happily retire with a total gain of {portfolio_value}')
# else:
    # print(f'It may take some more time for your retirement! Keep the hardwork. {portfolio_value}')
    
