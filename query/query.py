from fastapi import APIRouter
from config.db import conn
from schema.query_schema import queriesEntity
from pydantic import BaseModel


# from sklearn.feature_extraction.text import CountVectorizer
# from sklearn.metrics.pairwise import cosine_similarity
import math
import re
from collections import Counter

WORD = re.compile(r"\w+")

query_router  = APIRouter(
    prefix="/query",
    tags=['query']
)

class QueryModel(BaseModel):
    title : str
    description : str
    tags : list 
    posted_by : str 
    priority : str 
    posted_on : str
    status : str


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
    


@query_router.get("/stats")
def all_query_stats():
    return ["All Queries List"]

@query_router.get("/latest")
def latest_queries():
    result = conn.querybox.queries.find().limit(50)
    return queriesEntity(result)

class SkillsModel(BaseModel):
    skills : list

@query_router.post("/recommended")
async def recommended_queries(body : SkillsModel):
    skills = [skill.lower() for skill in body.skills]
    my_query = {"tags":{ "$in" : skills}}
    result = queriesEntity(conn.querybox.queries.find(my_query))
    new_result = []
    for idx in range(len(result)):
        item = result[idx]
        item["similarity_score"] = get_similarity_score(skills,item["tags"])
        new_result.append(item)
    new_result.sort(key=lambda x: x["similarity_score"],reverse=True)
    return new_result


@query_router.post("/create")
def create_post(query : QueryModel):
    print(query)
    conn.querybox.queries.insert_one(dict(query))
    return {"message" : True}


# @query_router.get("/search")
# def search_by_title():
#     return ["All Queries List"]


# @query_router.get("/priority")
# def queries_by_priority():
#     return ["All Queries List"]



