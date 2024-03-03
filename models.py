
class User:
    def __init__(self, username, bio):
        self.username = username
        self.bio = bio

        
    def __str__(self):
        return "User({}, {})".format(self.username, self.bio)