import sqlite3
from models import User

conn = sqlite3.connect("db/project.db")
cursor = conn.cursor()


class UserReqMaker:
    
    def __init__(self, dbname="project.db") -> None:
        self.conn = sqlite3.connect(dbname)
        self.cursor = conn.cursor()
    
    def add(self, obj: User):
        scheme = "INSERT INTO users(username, bio) VALUES(?, ?)"
        self.cursor.execute(scheme, (obj.username, obj.bio))
        self.save()
        created_obj = self.get("username", obj.username)
        print(created_obj)
        # print("inserted into users {} with id {}".format(obj, created_obj[0]))
    
    def get(self, field, value):
        if value == "all":
            cursor.execute("SELECT * FROM users")
            return cursor.fetchall()
        
        cursor.execute("SELECT * FROM users WHERE ?=?", (field, value))
        d = cursor.fetchone()
        print(d)
        return cursor.fetchone()
        
        
    def delete(self, field, value):
        cursor.execute("DELETE FROM users WHERE ?=?", (field, value))
        self.save()
        
    def save(self):
        self.conn.commit()
        


