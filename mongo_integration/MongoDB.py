from json import *

from pymongo import *


class MongoDB:
    def __init__(self, host, port, database, doc):
        cluster = MongoClient(host, port)
        db = cluster[database]
        self.__collection = db[doc]

    def find_all(self):
        ret = []
        coll = self.__collection.find({})
        for e in coll:
            ret.append(e)
        return dumps(ret)

    def find_by_criteria(self, key, value):
        coll = self.__collection.find({key: int(value)})
        for e in coll:
            return dumps(e)

    def find_by_id(self, id):
        return self.find_by_criteria("_id", id)

    def add(self, entity: dict):
        self.__collection.insert_one(entity)

    def remove_by_id(self, id):
        self.__collection.delete_one({"_id": id})
