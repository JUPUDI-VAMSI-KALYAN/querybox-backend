from fastapi import FastAPI
from query import query

# from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(query.query_router)

# origins = [
#     "http://localhost",
#     "http://localhost:4200",
#     "http://localhost:4200/"
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
print("Yes")
import socket
hostname=socket.gethostname()
IPAddr=socket.gethostbyname(hostname)
print("Your Computer Name is:"+hostname)
print("Your Computer IP Address is:"+IPAddr)


@app.get("/")
def index():
    return {"message":"Hello!"}


@app.get("/inservice")
def inservice():
    return True