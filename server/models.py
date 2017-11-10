from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float
import datetime
from database import Base

class Tenperatura(Base):
    __tablename__ = "tenperatura"
    id = Column(Integer, primary_key=True)
    tenp = Column(Float, nullable=False)
    data = Column(DateTime, default=datetime.datetime.utcnow)
    garagardoa = Column(Integer, ForeignKey("garagardoa.id"))

    def __init__(self, tenp, garagardoa):
        self.tenp = tenp
        self.garagardoa = garagardoa

class Garagardoa(Base):
    __tablename__ = "garagardoa"
    id = Column(Integer, primary_key=True)
    izena = Column(String(250), nullable=False)

    def __init__(self, izena):
        self.izena = izena
