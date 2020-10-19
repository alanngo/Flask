from repository.mongo.MongoDB import MongoDB

DATABASE = "SampleDB"
HOST = "localhost"
PORT = 27017
URI = "ENTER DB URI HERE"
USER = "user"
ASSET = "asset"

MONGO = MongoDB(
    host=HOST,
    port=PORT,
    database=DATABASE,
    docs=[USER, ASSET]
)
