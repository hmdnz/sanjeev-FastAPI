from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange
import psycopg2
from psycopg2.extras import RealDictCursor
import time
app = FastAPI()

class Post(BaseModel):
    title:str
    content:str

while True:
    
    try:
        conn =psycopg2.connect(host='localhost', database='fastapi',user='postgres',
        password='postgres',cursor_factory=RealDictCursor)
        cursor=conn.cursor()
        print('Database Connection Successful')
        break
    except Exception as error:
        print('Connection to the database failed')
        print("Error: ", error)
        time.sleep(5)
        
my_posts=[
    {"title":"title of post 1","content":"content of post1", "id":1},
    {"title":"Favourite foods","content":"I like pizza", "id":2},
    {"title":"Tropical Climate","content":"It can get as hot as 45c", "id":3},

]
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/post")
async def get_posts():
    return {"data": my_posts}

@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post:Post):
    cursor.execute(""" INSERT INTO posts (title, content, published) """)
    
    return{"data":"created post"}