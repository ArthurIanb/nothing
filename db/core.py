import sqlite3
from models import User

bd_fields = ['id', 'username', 'bio']


class UserReqMaker:
    def __init__(self, dbname="db/project.db") -> None:
        self.conn = sqlite3.connect(dbname)
        self.cursor = self.conn.cursor()
        
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        bio TEXT NOT NULL
        )
        ''')

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
        elif field in bd_fields:
            self.cursor.execute("SELECT * FROM users WHERE {}='{}'".format(field, value))
        t = self.cursor.fetchall()
        return t if t else [(0, "None", "None")]

    def delete(self, field, value):
        if field not in bd_fields:
            return "unsuccess"
        self.cursor.execute("DELETE FROM users WHERE {}='{}'".format(field, value))
        self.save()
        return "success"
    
    def flush(self):
        self.cursor.execute("DELETE FROM users WHERE true")
        self.save()
        return "success"
        
    def save(self):
        self.conn.commit()
