from flask import Blueprint, request

from service.asset import *

asset = Blueprint("asset", __name__)
asset_service = AssetService()


@asset.route("/asset", methods=["POST"])
def add_asset():
    u = request.get_json()
    return asset_service.add_asset(u), 201


@asset.route("/asset/<_id>", methods=["GET"])
def get_asset_by_id(_id):
    return asset_service.find_asset_by_id(_id)

