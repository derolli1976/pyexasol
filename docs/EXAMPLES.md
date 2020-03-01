## Preparation
Basic preparation steps are required to see examples in action.

1. Install PyEXASOL with [optional dependencies](/docs/DEPENDENCIES.md).
2. Download [PyEXASOL source code](https://github.com/badoo/pyexasol/archive/master.zip) and unzip it.
3. Make sure Exasol is installed and dedicated schema for testing is created. You may use free [Exasol Community Edition](https://www.exasol.com/portal/display/DOWNLOAD/Free+Trial) for testing purposes.
4. Open `/examples/` directory and edit file `\_config.py`. Input your Exasol credentials.
5. Run script to prepare data set for testing:
```
python examples/00_prepare.py
```

That's all. Now you may run examples in any order like common python scripts. E.g.:
```
python examples/01_basic.py
```

## Examples

- [01_basic.py](/examples/01_basic.py) - minimal code to create connection and run query;
- [02_fetch_tuple.py](/examples/02_fetch_tuple.py) - all methods of fetching result set returning tuples;
- [03_fetch_dict.py](/examples/03_fetch_dict.py) - all methods of fetching result set returning dictionaries;
- [04_fetch_mapper.py](/examples/04_fetch_mapper.py) - adding custom data type mapper for fetching;
- [05_formatting.py](/examples/05_formatting.py) - SQL text [formatting](/docs/SQL_FORMATTING.md);
- [06_pandas.py](/examples/06_pandas.py) - IMPORT / EXPORT to and from `pandas.DataFrame`;
- [07_import_export.py](/examples/07_import_export.py) - other methods of IMPORT / EXPORT;
- [08_transaction.py](/examples/08_transaction.py) - transaction management, autocommit;
- [09_exceptions.py](/examples/09_exceptions.py) - error handling, common errors;
- [10_redundancy.py](/examples/10_redundancy.py) - connection redundancy, how driver handles missing nodes;
- [11_edge_case.py](/examples/11_edge_case.py) - storing and fetching biggest and smallest values for data types available in Exasol;
- [12_db2_compat.py](/examples/12_db2_compat.py) - [DB-API 2.0 compatibility wrapper](/docs/DBAPI_COMPAT.md);
- [13_ext.py](/examples/13_ext.py) - extension functions to help with common Exasol-related problems outside of pure database driver scope;
- [14_parallel_export.py](/examples/14_parallel_export.py) - multi-process HTTP transport for export;
- [15_encryption.py](/examples/15_encryption.py) - SSL-encrypted WebSocket connection and HTTP transport;
- [16_ujson.py](/examples/16_ujson.py) - edge case example with `ujson`;
- [17_rapidjson.py](/examples/17_rapidjson.py) - edge case example with `rapidjson`;
- [18_session_params.py](/examples/18_session_params.py) - passing custom session parameters `client_name`, `client_version`;
- [19_local_config.py](/examples/19_local_config.py) - connect using local config file;
- [20_parallel_import.py](/examples/20_parallel_import.py) - multi-process HTTP transport for import;
- [21_parallel_export_import.py](/examples/21_parallel_export_import.py) - multi-process HTTP transport for export followed by import;
- [22_profiling.py](/examples/22_profiling.py) - last query profiling;
- [23_snapshot_transactions.py](/examples/23_snapshot_transactions.py) - snapshot transactions mode, which may help with metadata locking problems;
- [24_script_output.py](/examples/24_script_output.py) - run query with UDF script and capture output (may not work on local laptop);
- [25_overload.py](/examples/25_overload.py) - how to extend core PyEXASOL classes to add custom logic;
- [26_quote_ident.py](/examples/26_quote_ident.py) - how to enable quoted identifiers for `import_*`, `export_*` and other relevant functions;
- [27_abort_query.py](/examples/27_abort_query.py) - how to abort running query using separate thread;
- [28_thread_safety.py](/examples/28_thread_safety.py) - built-in protection from accessing connection object from multiple threads simultaneously;
- [29_dsn_parsing.py](/examples/29_dsn_parsing.py) - parsing of complex connection strings and catching relevant exceptions;
- [30_http_proxy.py](/examples/30_http_proxy.py) - connection via HTTP proxy;
- [31_context_manager.py](/examples/31_context_manager.py) - using WITH clause for `ExaConnection` and `ExaStatement` objects;
- [32_insert_multi](/examples/32_insert_multi.py) - INSERT small number of rows using prepared statements instead of HTTP transport;
- [33_meta](/examples/33_meta.py) - Lock-free meta data requests;
- [34_http_transport_errors](/examples/34_http_transport_errors.py) - various ways to break HTTP transport and recover from it;
- [35_garbage_collection](/examples/35_garbage_collection.py) - detect potential garbage collection problems due to cross-references;
