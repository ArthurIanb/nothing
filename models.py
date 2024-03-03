from .config import *


class User:
    def __init__(self, username, bio):
        self.username = username
        self.bio = bio
        if DEBUG:
            print("CREATED USER {} - {}".format(self.username, self.bio))
        
    def __str__(self):
        return "User({}, {})".format(self.username, self.bio)