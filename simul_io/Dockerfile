FROM python:3.6-jessie

RUN mkdir /app
WORKDIR /app

COPY validators.py .
COPY simul_io.py .
COPY 100000_orders.csv .

CMD python simul_io.py 100000