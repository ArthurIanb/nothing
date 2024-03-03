from db.core import UserReqMaker
from models import User

urm = UserReqMaker()
u = User("arthur", "arthur2")
urm.add(u)
cursor = urm.cursor
field = "id"
value = 2
cursor.execute("SELECT * FROM users WHERE {}={}".format(field, value))
# cursor.execute("SELECT * FROM users WHERE id=1")
print(cursor.fetchone())

