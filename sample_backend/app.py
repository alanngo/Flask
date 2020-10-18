from flask import *
from flask_cors import *

from api.user import *
from api.asset import *
from util.error_advice import advice

app = Flask(__name__)
app.register_blueprint(user)
app.register_blueprint(asset)
app.register_blueprint(advice)


@app.route("/api/<u_id>/<a_id>", methods=["PUT"])
def allocate_asset(u_id, a_id):
    ast = asset_service.find_asset_by_id(a_id)

    user_service.allocate_asset(u_id, ast)
    return user_service.get_user(u_id)


if __name__ == '__main__':
    CORS(app)  # lets other programs consume app
    app.debug = True
    app.run()
