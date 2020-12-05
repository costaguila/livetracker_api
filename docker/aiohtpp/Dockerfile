FROM python:3.9-buster

ENV PYTHONUNBUFFERED 1

RUN apt-get update \
    && apt-get install -y gcc python3-dev postgresql-client

COPY ./requirements /requirements

RUN pip install -r /requirements/production.txt;


COPY ./docker/aiohtpp/start_local /start_local
RUN sed -i 's/\r//' /start_local
RUN chmod +x /start_local


WORKDIR /app
