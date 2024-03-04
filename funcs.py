from db.core import UserReqMaker
from models import User

urm = UserReqMaker()

def create_user_command(inf: str):
    username, bio = inf[:inf.find(' ')], inf[inf.find(' ')+1:]
    new_user = User(username, bio)
    return urm.add(new_user)


def get_user_command(inf):
    splitted = inf.split()
    out = ""
    if len(splitted) == 1 and splitted[0] == "all":
        fields = urm.get("", "all")
    else:
        field, value = splitted
        fields = urm.get(field, value)
    for i in fields:
        out += "#{} {}\n".format(i[0], User(i[1], i[2]))
    return out

def remove_user_command(inf):
    field, value = inf.split()
    return urm.delete(field, value)


def flush_bd(inf):
    return urm.flush()
