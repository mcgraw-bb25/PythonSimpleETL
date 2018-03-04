import argparse
import csv
import time

import validators

from schema import complete_schema

parser = argparse.ArgumentParser(description="Create order set.")
parser.add_argument("orders", type=int, help="Number of orders to create.")
args = parser.parse_args()

file_to_read = "{}_orders.csv".format(args.orders)
file_to_write = "{}_orders_clean.csv".format(args.orders)


def write_csv(schema, orders, output_file):
    with open(output_file, "w") as csv_out:
        writer = csv.DictWriter(csv_out,
                                fieldnames=schema["db_schema"],
                                dialect="excel")
        writer.writeheader()
        writer.writerows(orders)
    return True


def load_incoming_data(filename):
    with open(filename, "r") as csv_in:
        reader = csv.DictReader(csv_in)
        data = [row for row in reader]
    return data


def validate_row(schema, validators, raw_row):
    clean_row = {}
    for column in schema["db_schema"]:
        for validator, columns in schema["validators"].items():
            if column in columns:
                clean_row[column] = validators[validator](raw_row[column])
                continue
    return clean_row


def validate_incoming_data(schema, validators, raw_data):
    clean_data = []
    for row in raw_data:
        clean_row = validate_row(schema, validators, row)
        clean_data.append(clean_row)
    return clean_data


if __name__ == "__main__":
    program = time.time()

    schema = complete_schema

    row_validators = {
        "float": validators.to_float,
        "int": validators.to_int,
        "date": validators.to_date,
        "varchar": validators.to_varchar
    }

    raw_orders = load_incoming_data(file_to_read)
    clean_orders = validate_incoming_data(schema, row_validators, raw_orders)
    success = write_csv(schema, clean_orders, file_to_write)

    program_end = time.time() - program
    print("stlid: {0:.2f}, Orders: {1:}".format(program_end, len(raw_orders)))
