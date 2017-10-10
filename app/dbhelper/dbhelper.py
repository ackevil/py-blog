from sqlalchemy.ext.declarative import declarative_base

from model.models import *

def init_db(engine):
    Base.metadata.create_all(bind=engine)
