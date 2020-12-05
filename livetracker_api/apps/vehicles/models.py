from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

import uuid

Base = declarative_base()

class VehicleModel(Base):
    __tablename__ = 'vehicle'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    live = Column(Boolean, default=True)
    trips = relationship("TripModel")

class TripModel(Base):
    """
        Represents a trip between point A and B.
        Posseses:
            # uuid(unique)
            # name
            # vehicle
            # a number of points
    """
    __tablename__ = 'trips'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(256), nullable=False)

    vehicle_id = Column(UUID(as_uuid=True), ForeignKey('vehicle.id'))
    vehicle = relationship("VehicleModel")

    points = relationship("PointModel")

class PointModel(Base):
    """
        Represents a location a Vehicle passed trought during a trip.
        Posseses:
            # uuid
            # timestamp
            # trip fk
            # lat / long
    """
    __tablename__ = 'point'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String(256), nullable=False)
    trip_id = Column(UUID(as_uuid=True), ForeignKey('trips.id'))
    trips = relationship("TripModel")
