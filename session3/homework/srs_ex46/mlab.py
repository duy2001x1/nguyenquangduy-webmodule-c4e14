import mongoengine

# mongodb://<dbuser>:<dbpassword>@ds161446.mlab.com:61446/account_renting

host = "ds161446.mlab.com"
port = 61446
db_name = "account_renting"
user_name = "admin"
password = "admin"


def mlab_connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())
