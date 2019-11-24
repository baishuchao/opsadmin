from sqlalchemy import Column, String, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import class_mapper
from datetime import datetime


Base = declarative_base()
def model_to_dict(model):
    model_dict = {}
    for key, column in class_mapper(model.__class__).c.items():
        model_dict[column.name] = getattr(model, key, None)
    return model_dict


class DBTag(Base):
    __tablename__ = 'asset_db_tag'

    id = Column(Integer, primary_key=True, autoincrement=True)
    db_id = Column('db_id', Integer)
    tag_id = Column('tag_id', Integer)



