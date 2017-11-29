# coding: latin-1
from database import Base, db_session, engine
from models import Tenperatura, Garagardoa
import os

def main():
    Base.metadata.create_all(engine)

    db_session.add(Garagardoa("Lehenengo garagardoa"))
    db_session.commit()

if __name__ == "__main__":
    main()
