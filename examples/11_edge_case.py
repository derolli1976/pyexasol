"""
Example 11
Try to read and write edge cases
"""

import pyexasol
import _config as config

import decimal

import pprint
printer = pprint.PrettyPrinter(indent=4, width=140)

edge_cases = [
    # Biggest values
    {
        'dec36_0': decimal.Decimal('+' + ('9' * 36)),
        'dec36_36': decimal.Decimal('+0.' + ('9' * 36)),
        'dbl': 1.7e308,
        'bl': True,
        'dt': '9999-12-31',
        'ts': '9999-12-31 23:59:59.999',
        'var100': 'ひ' * 100,
        'var2000000': 'ひ' * 2000000,
    },
    # Smallest values
    {
        'dec36_0': decimal.Decimal('-' + ('9' * 36)),
        'dec36_36': decimal.Decimal('-0.' + ('9' * 36)),
        'dbl': -1.7e308,
        'bl': False,
        'dt': '0001-01-01',
        'ts': '0001-01-01 00:00:00',
        'var100': '',
        'var2000000': 'ひ',
    },
    # All nulls
    {
        'dec36_0': None,
        'dec36_36': None,
        'dbl': None,
        'bl': None,
        'dt': None,
        'ts': None,
        'var100': None,
        'var2000000': None,
    }
]

# Very large query
C = pyexasol.connect(dsn=config.dsn, user=config.user, password=config.password, schema=config.schema)

try:
    stmt = C.execute('SELECT {val1} AS val1, {val2} AS val2, {val3} AS val3, {val4} AS val4, {val5} AS val5', {
        'val1': edge_cases[0]['var2000000'],
        'val2': edge_cases[0]['var2000000'],
        'val3': edge_cases[0]['var2000000'],
        'val4': edge_cases[0]['var2000000'],
        'val5': edge_cases[0]['var2000000'],
    })

    print(f'Query length: {len(stmt.query)}')
    print(f'Result column length: {len(stmt.fetchone()[0])}')

except pyexasol.ExaQueryError as e:
    print(e)

# Very large query with encryption
C = pyexasol.connect(dsn=config.dsn, user=config.user, password=config.password, schema=config.schema
                     , encryption=True)

try:
    stmt = C.execute('SELECT {val1} AS val1, {val2} AS val2, {val3} AS val3, {val4} AS val4, {val5} AS val5', {
        'val1': edge_cases[0]['var2000000'],
        'val2': edge_cases[0]['var2000000'],
        'val3': edge_cases[0]['var2000000'],
        'val4': edge_cases[0]['var2000000'],
        'val5': edge_cases[0]['var2000000'],
    })

    print(f'Query length: {len(stmt.query)}')
    print(f'Result column length: {len(stmt.fetchone()[0])}')

except pyexasol.ExaQueryError as e:
    print(e)


# Very large query with compression
C = pyexasol.connect(dsn=config.dsn, user=config.user, password=config.password, schema=config.schema
                     , compression=True)

try:
    stmt = C.execute('SELECT {val1} AS val1, {val2} AS val2, {val3} AS val3, {val4} AS val4, {val5} AS val5', {
        'val1': edge_cases[0]['var2000000'],
        'val2': edge_cases[0]['var2000000'],
        'val3': edge_cases[0]['var2000000'],
        'val4': edge_cases[0]['var2000000'],
        'val5': edge_cases[0]['var2000000'],
    })

    print(f'Query length: {len(stmt.query)}')
    print(f'Result column length: {len(stmt.fetchone()[0])}')

except pyexasol.ExaQueryError as e:
    print(e)
