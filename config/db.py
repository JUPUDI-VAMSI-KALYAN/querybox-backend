from time import monotonic
from pymongo import MongoClient

# conn = MongoClient()
conn = MongoClient("mongodb://kalyan123:kalyan1234@cluster0.nipgpbz.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS = 3000)
db = conn.querybox
# for e in db["queries"].find():
#     print(e)
# db.queries.database()
