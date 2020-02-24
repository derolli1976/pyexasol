import weakref


class ExaMetaData(object):
    """
    This class implements lock-free meta data requests using `/*snapshot execution*/` SQL hint described in IDEA-476
    https://www.exasol.com/support/browse/IDEA-476

    More methods will be added in future
    """
    def __init__(self, connection):
        self.connection = weakref.proxy(connection)

    def schema_exists(self, schema_name):
        object_name = self.connection.format.default_format_ident_value(schema_name)

        st = self._execute_snapshot("""
            SELECT 1
            FROM sys.exa_schemas
            WHERE schema_name={object_name}
        """, {
            'object_name': object_name,
        })

        return st.rowcount() > 0

    def table_exists(self, table_name):
        object_schema, object_name = self._format_ident(table_name)

        st = self._execute_snapshot("""
            SELECT 1
            FROM sys.exa_all_tables
            WHERE table_schema={object_schema}
                AND table_name={object_name}
        """, {
            'object_schema': object_schema,
            'object_name': object_name,
        })

        return st.rowcount() > 0

    def view_exists(self, view_name):
        object_schema, object_name = self._format_ident(view_name)

        st = self._execute_snapshot("""
            SELECT 1
            FROM sys.exa_all_views
            WHERE view_schema={object_schema}
                AND view_name={object_name}
        """, {
            'object_schema': object_schema,
            'object_name': object_name,
        })

        return st.rowcount() > 0

    def object_columns(self, object_name):
        object_schema, object_name = self._format_ident(object_name)

        st = self._execute_snapshot("""
            SELECT *
            FROM sys.exa_all_columns
            WHERE table_schema={object_schema}
                AND table_name={object_name}
        """, {
            'object_schema': object_schema,
            'object_name': object_name,
        })

        return st.fetchall()

    def query_columns(self, query, query_params=None):
        st = self.connection.cls_statement(self.connection, query, query_params, prepare=True)
        columns = st.columns()
        st.close()

        return columns

    def _format_ident(self, object_name):
        if isinstance(object_name, tuple):
            object_schema = self.connection.format.default_format_ident_value(object_name[0])
            object_name = self.connection.format.default_format_ident_value(object_name[1])
        else:
            object_schema = self.connection.current_schema()
            object_name = self.connection.format.default_format_ident_value(object_name)

        return object_schema, object_name

    def _execute(self, query, query_params=None):
        options = {
            'fetch_dict': True,
        }

        return self.connection.cls_statement(self.connection, query, query_params, **options)

    def _execute_snapshot(self, query, query_params=None):
        return self._execute(f"/*snapshot execution*/{query}", query_params)
