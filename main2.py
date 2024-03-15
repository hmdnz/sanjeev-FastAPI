from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    
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

@app.post("/posts")
def create_posts(post:Post):
    post_dict=post.dict()
    post_dict['id']=randrange(0, 100000000)
    my_posts.append()
    return{"data":post_dict}