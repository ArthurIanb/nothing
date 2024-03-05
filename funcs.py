from db.core import UserReqMaker
from models import User

urm = UserReqMaker()

def create_user_command(inf: str):
    if ' ' in inf or '\t' in inf:
        if ' ' in inf:
            s = ' '
        else:
            s = '\t'
        username, bio = inf[:inf.find(s)].strip(), inf[inf.find(s)+1:].strip()
        
    else:
        username = inf
        bio = "nobio"
    new_user = User(username, bio)
    return urm.add(new_user)


def get_user_command(inf):
    splitted = inf.split()
    fields = []
    out = ""
    if len(splitted) == 1:
        if splitted[0] == "all":
            fields = urm.get("", "all")
        else:
            return "Wrong command"
    elif len(splitted) == 2:
        field, value = splitted
        fields = urm.get(field, value)
    else:
        return "Wrong command"
    for i in fields:
        out += "#{} {}\n".format(i[0], User(i[1], i[2]))
    return out

def remove_user_command(inf):
    spltd = inf.split()
    if len(spltd) == 2:
        field, value = spltd
    else:
        return "Не правильное использование команды rem"
    return urm.delete(field, value)


def flush_bd(inf):
    return urm.flush()
