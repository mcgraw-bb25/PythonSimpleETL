import argparse
import datetime
import csv
import random
import time

from collections import namedtuple

parser = argparse.ArgumentParser(description='Create order set.')
parser.add_argument('orders', type=int, help='Number of orders to create.')
args = parser.parse_args()

schema = {
    "schema": ['key1','key2','key3','date1','date2','date3',
               'amount1','amount2','amount3','amount4','amount5',
               'amount6','description1','description2','ignored_varchar1',
               'ignored_varchar2','ignored_varchar3','ignored_varchar4',
               'ignored_numeric1','ignored_numeric2','ignored_numeric3',
               'ignored_numeric4']
}
Order = namedtuple("Order", schema["schema"])

words = []
with open("text", "r") as textfile:
    data = textfile.read()
    words = data.split(" ")

def generate_order():
    key1 = random.randint(1,500000)
    key2 = random.randint(1,500000)
    key3 = random.randint(1,500000)
    date1 = datetime.datetime(2017, random.randint(7,10), random.randint(1,27)).strftime("%Y-%m-%d")
    date2 = datetime.datetime(2017, random.randint(7,10), random.randint(1,27)).strftime("%Y-%m-%d")
    date3 = datetime.datetime(2017, random.randint(7,10), random.randint(1,27)).strftime("%Y-%m-%d")
    amount1 = random.randrange(500,2500)
    amount2 = random.randrange(500,2500)
    amount3 = random.randrange(500,2500)
    amount4 = random.randrange(500,2500)
    amount5 = random.randrange(500,2500)
    amount6 = random.randrange(500,2500)
    numwords1 = random.randint(50,150)
    numwords2 = random.randint(50,150)
    description1 = " ".join([random.choice(words) for i in range(1,numwords1)])
    description2 = " ".join([random.choice(words) for i in range(1,numwords2)])
    ignored_varchar1 = " ".join([random.choice(words) for i in range(1,numwords1)])
    ignored_varchar2 = " ".join([random.choice(words) for i in range(1,numwords2)])
    ignored_varchar3 = " ".join([random.choice(words) for i in range(1,numwords1)])
    ignored_varchar4 = " ".join([random.choice(words) for i in range(1,numwords2)])
    ignored_numeric1 = random.randrange(500,2500)
    ignored_numeric2 = random.randrange(500,2500)
    ignored_numeric3 = random.randrange(500,2500)
    ignored_numeric4 = random.randrange(500,2500)
    order = Order(key1, key2, key3, date1, date2, date3,
        amount1, amount2, amount3, amount4, amount5,
        amount6, description1, description2, ignored_varchar1,
        ignored_varchar2, ignored_varchar3, ignored_varchar4,
        ignored_numeric1, ignored_numeric2, ignored_numeric3,
        ignored_numeric4)

    return order

def generate_orders(number_of_orders):
    orders = []
    for order_number in range(1,number_of_orders+1):
        orders.append(generate_order()._asdict())
    return orders

def write_csv(orders, output_file):
    with open(output_file, "w") as csv_out:
        writer = csv.DictWriter(csv_out,
                                fieldnames=schema["schema"],
                                dialect="excel")
        writer.writeheader()
        writer.writerows(orders)


if __name__ == "__main__":
    start = time.time()
    n = args.orders
    orders = generate_orders(n)
    write_csv(orders, "{}_orders.csv".format(n))
    end = time.time() - start
    print ("Create Orders: {0:.2f} sec, {1:} orders, {2:.5f} sec per order".format(end, n, end/n))
