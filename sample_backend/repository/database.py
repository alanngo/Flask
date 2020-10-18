from repository.mongo.MongoDB import MongoDB

DATABASE = "SampleDB"
USER = "user"
ASSET = "asset"

MONGO = MongoDB\
(
    host="localhost",
    port=27017,
    database=DATABASE,
    docs=[USER, ASSET]
)
