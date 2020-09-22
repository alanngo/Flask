import json


class Student:

    def __init__(self, sid, name, language, framework, loves):
        self.id = sid
        self.name = name
        self.language = language
        self.framework = framework
        self.loves = loves

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)

    def __eq__(self, other):
        return str(self.id) == str(other.id)

    def __hash__(self):
        return hash(self.id)
