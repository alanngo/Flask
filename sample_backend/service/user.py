from repository.database import *


class UserService:
    def __init__(self):
        self.__user = MONGO.collection[USER]

    def add_user(self, user: dict):
        self.__user.add(user)
        return user

    def get_users(self):
        return self.__user.find_all()

    def get_user(self, _id):
        return self.__user.find_by_id(_id)

    def allocate_asset(self, u_id, asset):
        user = self.__user.find_by_id(u_id)
        if "assets" not in user.keys():
            assets = []
        else:
            assets = user["assets"]
        assets.append(asset)
        self.__user.update_entry(u_id, "assets", assets)
