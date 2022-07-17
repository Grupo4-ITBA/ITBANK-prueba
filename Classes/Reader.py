import json

class Reader:
    def __init__(self, file):
        self.file = json.load(open(file))

