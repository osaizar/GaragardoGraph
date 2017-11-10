from database import db_session
from sqlalchemy import and_, or_, func
from models import Tenperatura, Garagardoa

def add(data):
    try:
        db_session.add(data)
        db_session.commit()
        return int(data.id)
    except:
        db_session.flush()
        return False

def get_current_temps():
    #try:
    garId = db_session.query(func.max(Garagardoa.id)).scalar()
    temps = Tenperatura.query.filter(Tenperatura.garagardoa == garId).all()
    return temps
    #except:
    #    return False
