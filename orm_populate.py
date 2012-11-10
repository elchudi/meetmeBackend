import orm 
from sqlalchemy import (create_engine, MetaData, Column, Integer, String,
        Unicode, Numeric, func, literal, select)
from sqlalchemy.orm import sessionmaker, column_property
from sqlalchemy.ext.declarative import declarative_base


#engine = create_engine('sqlite:///:memory:', echo=False)
engine = create_engine('sqlite:///meetmeup.db', echo=False)
user_id = "10"
user_id2 = "20"
extra_data = "extraextra1"
name = "name1"
img = "img1"
user_type = "user_type1"
user1 = orm.User(user_id, extra_data, name, img, user_type)
user2 = orm.User(user_id2, extra_data, name, img, user_type)


connection = orm.Connection(user_id, user_id2)

session = sessionmaker(bind=engine)()
session.add_all([user1, user2, connection ])
session.commit()
