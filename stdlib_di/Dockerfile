FROM python:3.6-jessie

RUN mkdir /app
WORKDIR /app

#COPY requirements.txt requirements.txt
#RUN pip install -r requirements.txt

COPY schema.py .
COPY validators.py .
COPY standard_processor.py .
COPY 100000_orders.csv .

CMD python standard_processor.py 100000
