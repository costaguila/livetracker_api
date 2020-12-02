import os
from aiopg.sa import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import CreateTable
from sqlalchemy import Column, Integer, String, Boolean
import psycopg2


Base = declarative_base()

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    hash = Column(String(256), unique=True)
    live = Column(Boolean, default=True)

async def prepare_tables(pg):
    tables = [Vehicle.__table__,]
    async with pg.acquire() as conn:
        for table in tables:
            try:
                create_expr = CreateTable(table)
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
