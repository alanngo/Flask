import json


class Student:
    def __init__(self, name, language, framework, loves):
        self.name = name
        self.language = language
        self.framework = framework
        self.loves = loves

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
