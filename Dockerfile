FROM python:3.7-alpine

WORKDIR /usr/src

COPY ./requirements.txt .

RUN pip install wheel

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn"  , "-b", "0.0.0.0:80", "run:app"]