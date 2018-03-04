import argparse
import csv
import time

from collections import namedtuple

import validators

parser = argparse.ArgumentParser(description='Create order set.')
parser.add_argument('orders', type=int, help='Number of orders to create.')
args = parser.parse_args()

file_to_read = "{}_orders.csv".format(args.orders)
file_to_write = "{}_orders_clean.csv".format(args.orders)

schema = {
    "schema": ["key1", "key2", "key3", "date1", "date2", "date3",
               "amount1", "amount2", "amount3", "amount4", "amount5",
               "amount6", "description1", "description2", "ignored_varchar1",
               "ignored_varchar2", "ignored_varchar3", "ignored_varchar4",
               "ignored_numeric1", "ignored_numeric2", "ignored_numeric3",
               "ignored_numeric4"],
    "validators": {
        "float": ["amount1", "amount2", "amount3", "amount4",
                  "amount5", "amount6"],
        "int": ["key1", "key2", "key3"],
        "date": ["date1", "date2", "date3"],
        "varchar": ["description1", "description2"],
    },
    "db_schema": ["key1", "key2", "key3", "date1", "date2", "date3",
                  "amount1", "amount2", "amount3", "amount4", "amount5",
                  "amount6", "description1", "description2"]
}

Order = namedtuple("Order", schema["schema"])

validators = {
    "float": validators.to_float,
    "int": validators.to_int,
    "date": validators.to_date,
    "varchar": validators.to_varchar
}


def validate_row(raw_row):
    incoming_row = raw_row._asdict()
    clean_row = {}

    for column in schema["db_schema"]:
        for validator, columns in schema["validators"].items():
            if column in columns:
                clean_row[column] = validators[validator](incoming_row[column])
                continue
    return clean_row


def validate_incoming_data(file_in, file_out):
    rows = 0
    with open(file_in, "r") as csv_in, open(file_out, "w") as csv_out:
        writer = csv.DictWriter(csv_out,
                                fieldnames=schema["db_schema"],
                                dialect="excel",
                                quotechar='"')
        writer.writeheader()
        for line in csv_in.readlines():
            if rows > 0:
                row = Order._make(line.split(","))
                clean_row = validate_row(row)
                writer.writerow(clean_row)
            rows = rows + 1
    return rows - 1


if __name__ == "__main__":
    start = time.time()
    clean_orders = validate_incoming_data(file_to_read, file_to_write)
    end = time.time() - start
    print("SimulIO: Total, Time: {0:.2f}, Orders: {1:}".format(
            end, clean_orders))
