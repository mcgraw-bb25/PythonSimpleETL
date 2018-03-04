import argparse
import pandas
import time

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
        "amount1": validators.to_float,
        "amount2": validators.to_float,
        "amount3": validators.to_float,
        "amount4": validators.to_float,
        "amount5": validators.to_float,
        "amount6": validators.to_float,
        "key1": validators.to_int,
        "key2": validators.to_int,
        "key3": validators.to_int,
        "date1": validators.to_date,
        "date2": validators.to_date,
        "date3": validators.to_date,
        "description1": validators.to_varchar,
        "description2": validators.to_varchar
    },
    "db_schema": ["key1", "key2", "key3", "date1", "date2", "date3",
                  "amount1", "amount2", "amount3", "amount4", "amount5",
                  "amount6", "description1", "description2"]
}

if __name__ == "__main__":
    program = time.time()
    dataframe = pandas.read_csv(file_to_read,
                                header=0,
                                names=schema["schema"],
                                converters=schema["validators"])
    dataframe.to_csv(file_to_write, columns=schema["db_schema"], index=False)
    program_end = time.time() - program
    print("pandas: {0:.2f}, Orders: {1:}".format(program_end, len(dataframe)))
