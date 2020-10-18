from flask import Blueprint, request, jsonify

from service.user import UserService

user = Blueprint("user", __name__)
user_service = UserService()


@user.route("/user", methods=["POST"])
def add_user():
    u = request.get_json()
    return user_service.add_user(u), 201


@user.route("/user", methods=["GET"])
def get_all_users():
    return jsonify(user_service.get_users())


