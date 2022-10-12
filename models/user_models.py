from datetime import date, datetime
from sqlite3 import Timestamp
from typing import Optional
from pydantic import BaseModel,EmailStr



class NewUser(BaseModel):
    email : EmailStr
    username : str
    password : str
    skills : list
    is_avilabe : Optional[bool]
    posts : Optional[list]
    following : Optional[list] 
    rec_skills : Optional[list] 
    high : Optional[int] 
    mid : Optional[int] 
    low : Optional[int] 
    last_active : Optional[Timestamp]


class ExistingUser(BaseModel):
    email : EmailStr
    password : str
