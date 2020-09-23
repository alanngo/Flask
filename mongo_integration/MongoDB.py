from pymongo import *
from pymongo.errors import DuplicateKeyError


class MongoDB:
    # constructor
    def __init__(self, database, doc, url=None, host=None, port=None):

        if host or port is not None:
            cluster = MongoClient(host, port)
        else:
            cluster = MongoClient(url)
        db = cluster[database]
        self.__collection = db[doc]

    # retrieval functions

    '''
    retrieves every entry in the database
    @return every element in the database
    '''
    def find_all(self):
        ret = []
        coll = self.__collection.find({})
        for e in coll:
            ret.append(e)
        return ret

    '''
    find entries based on criteria
    @param key: criteria key
    @param value: criteria value
    @return the entries with the associated criteria
    '''
    def find_by_criteria(self, key, value):
        coll = self.__collection.find({key: value})
        ret = []
        for e in coll:
            ret.append(e)
        if len(ret) == 1:
            return ret[0]
        return ret

    '''
    find an entry based on the id
    @param id: the id to enter
    @return the entry w/ associated id
    '''
    def find_by_id(self, id):
        ret = self.find_by_criteria("_id", int(id))
        return ret

    # insertion functions

    '''
    adds an entry to the database with a auto-generated id
    @param entity: the object entity to add
    '''
    def default_add(self, entity: dict):
        self.__collection.insert_one(entity)

    '''
    adds an entry to the database with a user-defined id
    @param entity: the object entity to add
    '''
    def add_by_id(self, id, entity: dict):
        try:
            stub = {'_id': int(id)}
            stub.update(entity)
            self.default_add(stub)
        except DuplicateKeyError:
            pass

    '''
    adds an entry to the database by auto-incrementing the id
    @param entity: the object entity to add
    '''
    def add(self, entity: dict):
        index = self.size()
        self.add_by_id(index + 1, entity)

    # removal functions

    '''
    removes an entry based on an id
    @param id: the object associated with id to remove
    '''
    def remove_by_id(self, id):
        self.__collection.delete_one({"_id": int(id)})

    # properties functions

    '''
    size of collection
    @return number of elements in the collection
    '''
    def size(self):
        count = 0
        coll = self.find_all()
        for _ in coll:
            count = count + 1
        return count

    def empty(self):
        return self.size() == 0
