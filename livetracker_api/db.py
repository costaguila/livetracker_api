import os
from aiopg.sa import create_engine
from sqlalchemy.schema import CreateTable
import psycopg2

from apps.vehicles.models import VehicleModel

async def prepare_tables(pg):
    tables = [VehicleModel.__table__,]
    async with pg.acquire() as conn:
        for table in tables:
            try:
                create_expr = CreateTable(table)
                create_expr = str(create_expr).replace("CREATE TABLE","CREATE TABLE IF NOT EXISTS")
                await conn.execute(create_expr)
            except psycopg2.ProgrammingError:
                pass

async def init_pg(app):
    engine = await create_engine(
        database=os.environ.get('POSTGRES_DB'),
        user=os.environ.get('POSTGRES_USER'),
        password=os.environ.get('POSTGRES_PASSWORD'),
        host=os.environ.get('DB_HOST'),
        port=os.environ.get('DB_PORT','5432'))
    await prepare_tables(engine)
    app['db'] = engine

async def close_pg(app):
    app['db'].close()
    await app['db'].wait_closed()
    del app['db']
