FROM postgres
RUN echo POSTGRES_USER
COPY ./docker/postgres/postgis_extension.sql /docker-entrypoint-initdb.d
