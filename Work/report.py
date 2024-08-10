#!/usr/bin/env python
# report.py
#
# Exercise 2.4

# import csv
import locale
import tableformat
import fileparse as fp
import sys
import stock

def read_portfolio(filename):
    # portfolio = []
    # with open(filename, 'rt') as f:
        # rows = csv.reader(f)
        # headers = next(rows)
        # for rowno, row in enumerate(rows, start = 1):
            # record = dict(zip(headers, row))
            # try:
                # portfolio.append(
                    # {'name': record['name'],
                     # 'shares': int(record['shares']),
                     # 'price': float(record['price']),
                     # }
                # )
            # except ValueError:
                # print(f'Row# {rowno}: Bad Row: {row}')
    # return portfolio
    with open(filename) as f:
        records = fp.parse_csv(f, select=['name', 'shares', 'price'], types=[str, int, float])
    return [stock.Stock(r['name'], r['shares'], r['price']) for r in records]
        

def read_prices(filename):
    # prices = {}
    # with open(filename, 'rt') as f:
        # rows = csv.reader(f)
        # for row in rows:
            # if len(row) >= 2:
                # prices[row[0]] = float(row[1])
    # return prices
    with open(filename) as f:
        prices = fp.parse_csv(f, types=[str, float], has_headers=False, silence_errors=True)
    return dict(prices)

def make_report(portfolio, prices):
    report = []
    for pe in portfolio:
        report.append((pe.name, pe.shares, prices[pe.name], prices[pe.name] - pe.price))
    return report


def print_report(reportdata, formatter):
    '''
    Print a nicely formatted table from a list of (name, shares, price, change) tuples.
    '''
    formatter.headings(['Name', 'Shares', 'Price', 'Change'])
    # headers = ('Name', 'Shares', 'Price', 'Change')
    # print('%10s %10s %10s %10s' % headers)
    # print(f"{'-'*10} " * len(headers))
    # locale.setlocale(locale.LC_ALL, '') # currency printing
    for name, shares, price, change in reportdata:
        # print(f'{name:>10s} {shares:>10d} {locale.currency(price):>10s} {change:>10.2f}')
        rowdata = [ name, str(shares), f'{price:0.2f}', f'{change:0.2f}' ]
        formatter.row(rowdata)


def portfolio_report(portfolio_filename, prices_filename, fmt='txt'):
    # Read data files
    portfolio = read_portfolio(portfolio_filename)
    prices = read_prices(prices_filename)
    # create report data
    report = make_report(portfolio, prices)

    # Print it out
    # formatter = tableformat.TextTableFormatter()
    # formatter = tableformat.CSVTableFormatter()
    formatter = tableformat.create_formatter(fmt=fmt)
    print_report(report, formatter)

def main(argv):
    nArgs = len(argv)
    if nArgs < 3:
        sys.exit(f'Usagee: {sys.argv[0]} ''portfile pricefile')
    fname_portfolio = argv[1]
    fname_prices = argv[2]
    fmt = argv[3] if nArgs > 3 else 'txt'
    portfolio_report(fname_portfolio, fname_prices, fmt=fmt)
    
if __name__ == '__main__':
    main(sys.argv)
# portfolio_report('Data/portfolio.csv', 'Data/prices.csv')
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
    
