import sqlite3
from models import User

class UserReqMaker:
    
    def __init__(self, dbname="db/project.db") -> None:
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()
    
    def add(self, obj: User):
        scheme = "INSERT INTO users(username, bio) VALUES(?, ?)"
        self.cursor.execute(scheme, (obj.username, obj.bio))
        self.save()
        created_obj = self.get("username", obj.username)
        print("inserted into users {} with id {}".format(obj, created_obj[0]))
        return "success"
    
    def get(self, field, value):
        if value == "all":
            self.cursor.execute("SELECT * FROM users")
        else:
            self.cursor.execute("SELECT * FROM users WHERE {}='{}'".format(field, value))
        t = self.cursor.fetchall()
        print("D", t)
        return t if t else [(0, "nothing", "nothing")]
        
        
    def delete(self, field, value):
        self.cursor.execute("DELETE FROM users WHERE {}='{}'".format(field, value))
        self.save()
        return "success"
        
    def save(self):
        self.conn.commit()
        


