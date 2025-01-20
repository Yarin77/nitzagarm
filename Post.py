class Post:
    def __init__(self, username, location, description):
        self.username = username
        self.location = location
        self.description = description
        self.likes_counter = 0
        self.comments = []

    def add_like(self):
        self.likes_counter += 1

    def add_comment(self, text):
        self.comments.append(text)

    def display(self):
        pass
