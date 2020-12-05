from aiohttp import web
from db import init_pg, close_pg

from apps.vehicles.models import VehicleModel, TripModel, PointModel

import string
import random


async def hello(request):
    return web.Response(text="Hello, world")

async def ListVehicles(request):
    db = request.app['db']
    sessionmaker = request.app['session']
    session = sessionmaker()
    result = session.query(VehicleModel)
    print(result)
    for item in result:
        print(item.id)
    return web.Response(text="Hello, world")

async def CreateVehicles(request):
    db = request.app['db']
    sessionmaker = request.app['session']
    session = sessionmaker()


    veh = VehicleModel()

    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    trp = TripModel(name=name)

    name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))
    ptn = PointModel(name = name)

    #adicionar trip para vehicle
    veh.trips.append(trp)
    trp.points.append(ptn)
    session.add(veh)
    session.commit()
    session.add(trp)
    session.commit()
    session.add(ptn)
    session.commit()

    return web.Response(text="Hello, world")


app = web.Application()
app.add_routes([web.get('/', ListVehicles)])
app.add_routes([web.get('/create', CreateVehicles)])
app.on_startup.append(init_pg)
app.on_cleanup.append(close_pg)

if __name__ == '__main__':
    web.run_app(app)
