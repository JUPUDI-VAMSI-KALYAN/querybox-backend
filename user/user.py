from fastapi import APIRouter,Depends
from schemas.user_schema import latest_usersEntity
from config.db import conn
from pydantic import EmailStr,BaseModel
import pymongo
import re
import math
from collections import Counter


user_router = APIRouter(
    prefix="/user",
    tags=['User']
)
# password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

WORD = re.compile(r"\w+")

def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in list(vec1.keys())])
    sum2 = sum([vec2[x] ** 2 for x in list(vec2.keys())])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator

def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)

def get_similarity_score(lis1,lis2):
    l1 = text_to_vector(" ".join(lis1))
    l2 = text_to_vector(" ".join(lis2))
    return get_cosine(l1,l2)


# def get_hashed_password(password: str) -> str:
#     return password_context.hash(password)


# def verify_password(password: str, hashed_pass: str) -> bool:
#     return password_context.verify(password, hashed_pass)





@user_router.get("/stats")
def all_users_stats():
    return ["all users list"]


# @user_router.post("/login")
# async def login(user : ExistingUser):
#     db_user = dict(conn.Test.User.find_one({"email" : user.email}))
#     print(db_user)
#     if db_user:
#         if verify_password(user.password,db_user["password"]):
#             access_token = create_access_token(
#                 data = {
#                     "username" : db_user["username"],
#                     "user_id" : str(db_user["_id"])
#             })
#             return {
#                 'access_token' : access_token,
#                 "token_type" : "bearer",
#                 'user_id' : str(db_user["_id"]),
#                 'username': db_user["username"]
#             }
#         else:
#             raise HTTPException(status_code= status.HTTP_406_NOT_ACCEPTABLE, detail='InCorrect Passowrd')
#     raise HTTPException(status.HTTP_404_NOT_FOUND, detail='User not found.')


@user_router.get("/all")
def all():
    # for obj in conn.Test.Users.find():
    #     print(obj)
    tags = ["python"]
    my_query = {"skills":{ "$in" : list(tags)}}
    return latest_usersEntity(conn.Test.Users.find(my_query).limit(10))




# @user_router.post("/register")
# def create_user(user : NewUser):
#     password = get_hashed_password(user.password)
#     new_user = dict(user)
#     new_user["password"]= password
#     result = conn.Test.User.insert_one(new_user)
#     # print(conn.Test.User.find_one({"email" : user.email}))
#     db_user = dict(conn.Test.User.find_one({"email" : new_user["email"]}))
#     access_token = create_access_token(
#                 data = {
#                     "username" : db_user["username"],
#                     "user_id" : str(db_user["_id"])
#             })
#     return {
#         'access_token' : access_token,
#         "token_type" : "bearer",
#         'user_id' : str(db_user["_id"]),
#         'username': db_user["username"]
#         # "data" : db_user
#         }
#     # return userEntity(conn.Test.User.find_one({"email" : user.email}))




class UserModel(BaseModel):
    username :  str = None
    is_available : bool = None
    email : EmailStr = None
    skills : list = None
    experiance : int = None
    gender : str = None
    response_time : int = None
    high : int = None
    mid : int = None
    low : int = None
    last_active : int = None


@user_router.post("/create")
def create_user(user : UserModel):
    # print(user)
    conn.querybox.users.insert_one(dict(user))
    return {"message" : True}


class TagModel(BaseModel):
    tags : list
@user_router.post("/find_experts")
async def get_expert(body : TagModel):
    print(body.tags)
    tags = [tag.lower() for tag in body.tags]
    my_query = {"skills":{ "$in" : list(tags)}}
    print(type(body.tags))
    sorting_order = [("experiance",pymongo.DESCENDING),("high",pymongo.DESCENDING),("mid",pymongo.DESCENDING),("low",pymongo.DESCENDING),("response_time",pymongo.ASCENDING)]
    result = latest_usersEntity(conn.querybox.users.find(my_query).sort(sorting_order))
    print(len(result))
    new_result = []
    for idx in range(len(result)):
        item = result[idx]
        item["similarity_score"] = get_similarity_score(tags,item["skills"])
        new_result.append(item)
    new_result.sort(key=lambda x: x["similarity_score"],reverse=True)
    return new_result

