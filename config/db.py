from time import monotonic
from pymongo import MongoClient

# conn = MongoClient()
conn = MongoClient("mongodb+srv://latha:mydhili9@cluster0.85cgdbw.mongodb.net/?retryWrites=true&w=majority",serverSelectionTimeoutMS = 3000)
db = conn.querybox
# for e in db["queries"].find():
#     print(e)
# db.queries.database()
