from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Boolean


Base = declarative_base()

class VehicleModel(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    hash = Column(String(256), unique=True)
    live = Column(Boolean, default=True)
