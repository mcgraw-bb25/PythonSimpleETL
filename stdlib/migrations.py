import subprocess

from pprint import pprint

from schema import complete_schema, matching_schema

sql_datatypes = {
    "float": "numeric",
    "int": "integer",
    "date": "timestamp without time zone",
    "varchar": "character varying"
}

migration_datatypes = {
    "float": "numeric",
    "int": "int",
    "date": "timestamp",
    "varchar": "varchar(255)"
}


def fetch_current_table_query(query):
    command = ["psql", "-U", "matt", "-w", "-c", query]
    results = subprocess.run(command, stdout=subprocess.PIPE)
    results_string = results.stdout.decode()
    results_list = results_string.split("\n")
    return results_list


def generate_table_comparison_query(table_name):
    query = """select column_name, data_type
               from information_schema.columns
               where table_name = '{}';"""
    return query.format(table_name)


def parse_table(query_results):
    column_info = query_results[2:-3]
    current_schema = [parse_column(column) for column in column_info]
    return current_schema


def parse_column(column_as_string):
    column_name, data_type = column_as_string.split("|")
    return (column_name.strip(), data_type.strip())


def fetch_datatype(column, schema, datatype_dict, default_type):
    column_datatype = default_type
    for datatype, columns in schema["validators"].items():
        if column in columns:
            column_datatype = datatype
            break
    return column, datatype_dict[column_datatype]


def fetch_migration_datatype(column, schema):
    default_type = "varchar"
    return fetch_datatype(column, schema, migration_datatypes, default_type)


def fetch_sql_datatype(column, schema):
    default_type = "character varying"
    return fetch_datatype(column, schema, sql_datatypes, default_type)


def generate_etl_schema(schema):
    etl_schema = [fetch_sql_datatype(column, schema)
                  for column in schema["db_schema"]]
    return etl_schema


def check_for_migrations(db_schema, etl_schema):
    return db_schema != etl_schema


def build_new_table(etl_schema, schema):
    query_header = "drop table {}; \ncreate table {} (\n"
    query_footer = "\n);"
    query_columns = []
    query_column = "\t{} {} {}"
    column_counter = 0
    for column in etl_schema:
        column_name, datatype = fetch_migration_datatype(column[0], schema)
        query_prefix = "," if column_counter != 0 else ""
        new_column = query_column.format(query_prefix, column_name, datatype)
        query_columns.append(new_column)
        column_counter = column_counter + 1
    new_header = query_header.format(schema["tablename"], schema["tablename"])
    new_columns = "\n".join(query_columns)
    query = new_header + new_columns + query_footer
    return query


if __name__ == "__main__":

    schema = complete_schema

    query = generate_table_comparison_query('orders')
    query_results = fetch_current_table_query(query)
    db_schema = parse_table(query_results)

    etl_schema = generate_etl_schema(schema)

    schema_required = check_for_migrations(db_schema, etl_schema)

    pprint(schema_required)

    new_table = build_new_table(etl_schema, schema)
    print(new_table)
