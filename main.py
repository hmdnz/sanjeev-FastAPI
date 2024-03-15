from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Post(BaseModel):
    title:str
    content:str
    
my_posts=[{"title"}]
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/post")
async def get_posts():
    return {"data": "This is your posts"}

@app.post("/posts")
def create_posts(post:Post):
    print(post)
    print(post.dict())
    return{"data":post}