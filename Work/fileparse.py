# fileparse.py
#
# Exercise 3.3

import csv
from typing import Iterable

def parse_csv(lines, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    '''
    Parse a CSV file into a list of records
    '''

    if type(lines) is str or not isinstance(lines, Iterable):
        raise RuntimeError('Invalid input. Only accepts an Iterable except names')
    # Read the file headers
    if select and not has_headers:
        raise RuntimeError('select arguments require column headers')
    rows = csv.reader(lines, delimiter=delimiter)
    if has_headers:
        headers = next(rows)
    if select:
        headers_with_indices=dict(zip(headers, range(len(headers))))
        indices=[ headers_with_indices[column] for column in select ]
    else:
        indices=[]
    records=[]
    for rowno, row in enumerate(rows, 1):
        if not row: # Skip blank rows
            continue
        if indices:
            row = [ row[index] for index in indices ]
        try:
            if types:
                row=[ func(val) for func, val in zip(types, row) ]
        except ValueError as e:
            if not silence_errors:
                print(f"Row {rowno}: Couldn't convert {row}")
                print(f"Row {rowno}: Reason {e}")
            continue
        if has_headers:
            record = dict(zip(headers, row))
        else:
            record = tuple(row)
        records.append(record)
    return records


