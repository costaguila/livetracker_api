import os
from sqlalchemy import create_engine

from sqlalchemy.schema import CreateTable
import psycopg2

from apps.vehicles.models import VehicleModel, TripModel, PointModel

from sqlalchemy.orm import sessionmaker


def prepare_tables(pg):
    tables = [VehicleModel.__table__,TripModel.__table__, PointModel.__table__]
    with pg.connect() as conn:
        for table in tables:
            try:
                create_expr = CreateTable(table)
                create_expr = str(create_expr).replace("CREATE TABLE","CREATE TABLE IF NOT EXISTS")
                conn.execute(create_expr)
            except psycopg2.ProgrammingError:
                pass

async def init_pg(app):
    CONNECTION_STRING = f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('DB_HOST')}:{os.environ.get('DB_PORT','5432')}/{os.environ.get('POSTGRES_DB')}"
    engine =  create_engine(CONNECTION_STRING)
    prepare_tables(engine)
    app['session'] =  sessionmaker(bind=engine)
    app['db'] = engine

async def close_pg(app):
    app['db'].close()
    app['db'].wait_closed()
    del app['db']
