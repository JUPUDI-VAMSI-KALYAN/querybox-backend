from time import monotonic
from pymongo import MongoClient

# conn = MongoClient()
conn = MongoClient("mongodb://kalyan123:kalyan1234@cluster0.nipgpbz.mongodb.net/?retryWrites=true&w=majority&tls=fals&ssl=false")
db = conn.querybox
# for e in db["queries"].find():
#     print(e)
db.queries.database()