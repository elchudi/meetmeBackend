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

@get('/account_amount')
def account_amount():
    account_number = request.params.get('account_number')
    amount = get_account_amount(account_number)
    print amount
    return "".join(str(amount))

@get('/accounts_for_telephone')
def accounts_for_telephone():
    telephone = request.params.get('telephone')
    accounts =  get_accounts_for_tel(telephone)
    print accounts
    to_ret = '{"piggy":['
    for a in accounts:
        telephones = get_tel_for_account(a.account_number)
        encoded = ORMEncoder().encode(a)
        encoded = encoded[:-1]
        encoded += ',"telephones":['
        for t in telephones :
            encoded += '{"telephone":'
            encoded += t
            encoded += '},'
        encoded = encoded[:-1]
        encoded += ']}'
        print encoded
        #print json.dumps(a.__dict__, skipkeys=True)
        to_ret += encoded
        to_ret += ","
    to_ret = to_ret[:-1]
    to_ret += ']}'
    print to_ret
    return to_ret
"""
@post('/get_connections')
def get_connections():
    user_id = request.json['user_id']
    print user_id
    connections =  get_connection(user_id)
    print connections
    to_ret = '{"meetmeup":['
    for c in connections

        user = get_user(c.user_2))
        encoded = ORMEncoder().encode(user)
        print encoded
        #print json.dumps(a.__dict__, skipkeys=True)
        to_ret += encoded
        to_ret += ","
    to_ret = to_ret[:-1]
    to_ret += ']}'
    print to_ret
    return to_ret
"""

@post('/get_connections')
def get_connections():
    user_id = request.json['user_id']
    print user_id
    connections =  get_connection(user_id)
    print connections
    to_ret = '{"meetmeup":['
    for c in connections

        encoded = ORMEncoder().encode(c)
        print encoded
        #print json.dumps(a.__dict__, skipkeys=True)
        to_ret += encoded
        to_ret += ","
    to_ret = to_ret[:-1]
    to_ret += ']}'
    print to_ret
    return to_ret


@get('/get_user')
def get_user():
    user_id = request.params.get('user_id') 
    user = get_user(user_id)   
    return ORMEncoder().encode(account)


@get('/get_users')
def get_users():
    print user_id
    connections =  get_connection(user_id)
    print connections
    print to_ret
    return to_ret

@post('/update_account_amount')
def update_account_amount():
    account_number =  request.json['account_number']
    amount = request.json['amount']
    return str(account_amount_update(account_number, amount))

@post('/add_users_to_account')
def add_user_to_account_get():
    telephone = request.json['telephone']
    account_number = request.json['account_number']
    return str(add_user_to_account(account_number, telephone))


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
    
@post('/add_account')
def add_account():
    print "adding account"
    print request.json
    print dir(request.json)
    telephone = request.json['telephone']
    name = request.json['name']
    amount = request.json['amount']
    amount_nedded = request.json['amount_nedded']
    account_number = request.json['account_number']
    
    session = orm.get_orm_session()
    user_id = user_id(telephone)[0].id
    acc = orm.Account( account_number,  amount_needed, name, None, user_id, amount)
    session.add_all([acc])
    session.commit()
    session.bind.dispose()
    print "account added ", telephone, account_number
    return "OK"


class ORMEncoder(JSONEncoder):
    def default(self, o):
        dic = o.__dict__
        del(dic['_sa_instance_state'])
        return dic
 

def account_amount_update(account_number, amount):
    session = orm.get_orm_session()
    accounts = session.query(orm.Account).filter_by(account_number=account_number).all()
    if accounts:
        for account in accounts:
            account.amount = amount
        session.commit()
        session.bind.dispose()
        return True
    else:
        session.bind.dispose()
        return False
    
def get_account(account_number):
    session = orm.get_orm_session()
    account = session.query(orm.Account).filter_by(account_number=account_number).first()
    session.bind.dispose()
    return account

def get_account_amount(account_number):
    session = orm.get_orm_session()
    amount = session.query(orm.Account.amount).filter_by(account_number=account_number).first()
    session.bind.dispose()
    print amount
    return amount[0]

def get_account_id_from_account_number(account_number):
    session = orm.get_orm_session()
    account_id = session.query(orm.Account.id).filter_by(account_number=account_number).first()
    session.bind.dispose()
    if account_id:
        print "account_id", account_id[0]
        return account_id[0]
    return None

def get_accounts_for_tel(telephone):
    print "get_account from tel"
    session = orm.get_orm_session()
    accounts = session.query(orm.Account).join(orm.SharedAccount).join(orm.User).filter(orm.User.telephone==telephone).all()
    """
    account_ids = session.query(orm.SharedAccount.account_id).filter_by(telephone=telephone).all()
    print "accounts_ids", account_ids
    if not account_ids:
        return None
    accounts = session.query(orm.Account).filter(orm.Account.id.in_([x[0] for x in account_ids])).all()
    """
    session.bind.dispose()
    print accounts
    to_ret = []
    for acc in accounts:
        to_ret.append(acc)
    return to_ret
   
def get_connection(user_id):
    session = orm.get_orm_session()
    connections = session.query(orm.Connection).join(orm.User).filter(orm.User.user_id==user_1).all()
    print "connections", connections
    session.bind.dispose()
    if connections:
        return connections 
    return None

def get_tel_for_account(account_number):
    session = orm.get_orm_session()
    telephones = session.query(orm.User.telephone).join(orm.Account).filter(orm.Account.account_number==account_number).all()
    """
    account_id = get_account_id_from_account_number(account_number)
    if not account_id:
        return None
    telephones = session.query(orm.SharedAccount.telephone).filter_by(account_id=account_id).all()
    """
    session.bind.dispose()
    print telephones
    to_ret = []
    for tel in telephones:
        to_ret.append(tel[0])
    print to_ret
    return to_ret

def get_user_for_id(user_id):
    session = orm.get_orm_session()
    users = session.query(orm.User).filter_by(user_id=user_id).all()
    session.bind.dispose()
    if users:
        return users
    return None

def add_user_to_account(account_number, telephone):
def add_connection(user_1, user_2):
    connection = orm.Connection(user_1, user_2)
    connection_back = orm.Connection(user_2, user_1)
    session = orm.get_orm_session()
    session.add_all([connection, connection_back])
    session.commit()
    session.bind.dispose()
    return True
 
if __name__ == "__main__":
    run(host='0.0.0.0', port=8080)
