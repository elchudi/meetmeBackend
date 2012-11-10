from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import ForeignKey
from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime


# Setup the database engine and session


from sqlalchemy import (create_engine, MetaData, Column, Integer, String,
        Unicode, Numeric, func, literal, select)
from sqlalchemy.orm import sessionmaker, column_property
from sqlalchemy.ext.declarative import declarative_base


#engine = create_engine('sqlite:///:memory:', echo=False)
engine = create_engine('sqlite:///meetmeup.db', echo=False)
session = sessionmaker(bind=engine)()

print "testing that engine works", engine.execute("select 1").scalar()

Base = declarative_base()

def get_orm_session():
    engine = create_engine('sqlite:///meetmeup.db', echo=False)
    session = sessionmaker(bind=engine)()
    return session 

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    user_id = Column(String)
    extra_data = Column(String)
    name = Column(String)
    img = Column(String)
    user_type = Column(String)
 
    def __init__(self, user_id, extra_data, name, img, user_type):
        self.user_id  = user_id
        self.extra_data = extra_data
        self.name  = name
        self.img  = img
        self.user_type = user_type




class Connection(Base):
    __tablename__ = 'connection'
    
    id = Column(Integer, autoincrement=True, primary_key=True, unique=True)
    user_1 = Column(String, ForeignKey('users.user_id'), nullable=False  )
    user_2 = Column(String, ForeignKey('users.user_id'), nullable=False  )
    

    def __init__(self, user_1, user_2):
        self.user_1 = user_1
        self.user_2 = user_2

    def __repr__(self):
        return "<Connection('%d','%d','%d')>" % (self.id, self.account_id, self.user_id)

Base.metadata.create_all(engine) 

#session.add_all([user1])

#print zone1

accounts =  engine.execute("select * from users")
for row in accounts:
    print row
accounts =  engine.execute("select * from connection")
for row in accounts:
    print row

