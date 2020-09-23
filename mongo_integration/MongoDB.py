from pymongo import *


class MongoDB:
    def __init__(self, host, port, database, coll):
        cluster = MongoClient(host, port)
        db = cluster[database]
        self.__collection = db[coll]

    def find_all(self):
        ret = []
        coll = self.__collection.find({})
        for e in coll:
            ret.append(e)
        return ret

    def find_by_criteria(self, key, value):
        ret = []
        coll = self.__collection.find({key: value})
        for e in coll:
            ret.append(e)
        return ret

    def find_by_id(self, id):
        return self.find_by_criteria("_id", id)



    def add(self, entity: dict):
        self.__collection.insert_one(entity)
