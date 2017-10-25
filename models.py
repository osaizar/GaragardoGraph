from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Date
from database import Base

class Tenperatura(Base):
    __tablename__ = "tenperatura"
    id = Column(Integer, primary_key=True)
    tenp = Column(Integer, nullable=False)

    def __init__(self, tenp):
        pass
