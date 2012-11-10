from bottle import route, run, get, request, post
import os
import json
import orm
from json import JSONEncoder



"""
@post('/add_account')
def add_account():
    pass

    
Method should not be really implemented, only for testing purposes
"""
@get('/get_users')
def get_users():
    session = orm.get_orm_session()
    users = session.query(orm.User).all()
    to_ret = '{"meetmeup":['
    for u in users:
        encoded = ORMEncoder().encode(u)
        print encoded
        #print json.dumps(a.__dict__, skipkeys=True)
        to_ret += encoded
        to_ret += ","
    to_ret = to_ret[:-1]
    to_ret += ']}'
    session.bind.dispose()
    return to_ret


@post('/get_connections')
def get_connections():
    user_id = request.json['user_id']
    print user_id
    connections =  get_connection(user_id)
    print connections
    to_ret = '{"meetmeup":['
    for c in connections:
        encoded = ORMEncoder().encode(c)
        print encoded
        #print json.dumps(a.__dict__, skipkeys=True)
        to_ret += encoded
        to_ret += ","
    to_ret = to_ret[:-1]
    to_ret += ']}'
    print to_ret
    return to_ret


@post('/get_user')
def get_user():
    user_id = request.json['user_id']
    user = get_user(user_id)   
    return ORMEncoder().encode(user)


@post('/add_connection')
def add_user_to_account_get():
    user_1 = request.json['user_1']
    user_2 = request.json['user_2']
    return str(add_user_to_account(account_number, telephone))

@post('/add_user')
def add_user():
    print "adding user"
    print request.json
    print dir(request.json)
    user_id = request.json['user_id']
    extra_data = request.json['extra_data']
    name = request.json['name']
    img = request.json['img']
    user_type = request.json['user_type']
    session = orm.get_orm_session()
    user = orm.User(user_id, extra_data, name, img, user_type)
    session.add_all([user])
    session.commit()
    session.bind.dispose()
    print "useradde ", telephone, token
    return "OK"
    

class ORMEncoder(JSONEncoder):
    def default(self, o):
        dic = o.__dict__
        del(dic['_sa_instance_state'])
        return dic
 
   
def get_connection(user_id):
    session = orm.get_orm_session()
    connections = session.query(orm.Connection).join(orm.User).filter(orm.User.user_id==user_1).all()
    print "connections", connections
    session.bind.dispose()
    if connections:
        return connections 
    return None


def get_user_for_id(user_id):
    session = orm.get_orm_session()
    users = session.query(orm.User).filter_by(user_id=user_id).all()
    session.bind.dispose()
    if users:
        return users
    return None

def add_connection(user_1, user_2):
    connection = orm.Connection(user_1, user_2)
    connection_back = orm.Connection(user_2, user_1)
    session = orm.get_orm_session()
    session.add_all([connection, connection_back])
    session.commit()
    session.bind.dispose()
    return True
 
if __name__ == "__main__":
    run(host='0.0.0.0', port=8090)
