FROM python:3.6-jessie

RUN mkdir /app
WORKDIR /app

#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt

COPY validators.py .
COPY schema_inversion.py .
COPY 100000_orders.csv .

CMD python schema_inversion.py 100000