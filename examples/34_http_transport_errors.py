"""
Example 34
Edge cases for HTTP transport, killing & failing various components at different times
"""

import os
import psutil
import shutil
import threading

import pyexasol
import _config as config

import pprint
printer = pprint.PrettyPrinter(indent=4, width=140)

main_process = psutil.Process()
dev_null = open(os.devnull, 'wb')

C = pyexasol.connect(dsn=config.dsn, user=config.user, password=config.password, schema=config.schema)


###
# Normal execution
###


def observer_callback(pipe, dst, **kwargs):
    print(main_process.children())
    print(threading.enumerate())

    shutil.copyfileobj(pipe, dev_null)

    return


C.export_to_callback(observer_callback, None, 'SELECT * FROM users LIMIT 10')

print(main_process.children())
print(threading.enumerate())


###
# Kill HTTP transport
###


def http_terminate_callback(pipe, dst, **kwargs):
    main_process.children()[0].terminate()
    shutil.copyfileobj(pipe, dev_null)

    return


try:
    C.export_to_callback(http_terminate_callback, None, 'SELECT * FROM users LIMIT 10')
except pyexasol.ExaError as e:
    print(e)


print('Finished Kill HTTP transport')


###
# Abort SQL query
###


def abort_query_callback(pipe, dst, **kwargs):
    C.abort_query()
    shutil.copyfileobj(pipe, dev_null)

    return


try:
    C.export_to_callback(abort_query_callback, None, 'SELECT * FROM users LIMIT 10')
except pyexasol.ExaError as e:
    print(e)

print('Finished Abort Query')


###
# Close WS connection
###


def close_connection_callback(pipe, dst, **kwargs):
    C.close()
    shutil.copyfileobj(pipe, dev_null)

    return


try:
    C.export_to_callback(close_connection_callback, None, 'SELECT * FROM users LIMIT 10')
except Exception as e:
    print(e)

print('Finished Close Connection')
