from datetime import date
from enum import Enum
from sqlite3 import Date
from pydantic import BaseModel

class QueryModel(BaseModel):
    title : str
    description : str
    tags : list 
    posted_by : str 
    priority : str 
    posted_on : str
    status : str