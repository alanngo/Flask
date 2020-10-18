from repository.database import *


class AssetService:
    def __init__(self):
        self.__asset = MONGO.collection[ASSET]

    def add_asset(self, asset: dict):
        self.__asset.add(asset)
        return asset

    def find_asset_by_id(self, _id):
        return self.__asset.find_by_id(_id)
