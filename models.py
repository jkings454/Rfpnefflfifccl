"""
models.py


"""
from sqlalchemy import Column, Float, String, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class DataPoint(Base):
    """
    A datapoint that the user has determined.
    """
    __tablename__= "data_point"

    id = Column(Integer(), primary_key=True)

    name = Column(String(80), default="Anonymous")

    N = Column(Float(), nullable=False) # Calculated.
    Rstar = Column(Float(), nullable=False)
    fp = Column(Float(), nullable=False)
    ne = Column(Float(), nullable=False)
    fl = Column(Float(), nullable=False)
    fi = Column(Float(), nullable=False)
    fc = Column(Float(), nullable=False)
    L = Column(Float(), nullable=False)

    created_on = Column(DateTime(timezone=True), server_default=func.now())

    @property
    def serialize(self):
        """
        Serializes itself
        :return: A dictionary with all of the column data.
        """
        return {
            "id": self.id,
            "name": self.name,
            "N": self.N,
            "Rstar": self.Rstar,
            "fp": self.fp,
            "ne": self.ne,
            "fl": self.fl,
            "fi": self.fi,
            "fc": self.fc,
            "L": self.L,
            "created_on" : self.created_on
        }