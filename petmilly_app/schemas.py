from pydantic import BaseModel
from typing import List, Optional


class User(BaseModel):
    name: str
    email: str
    password : str

class Comment(BaseModel):
    user_id : int
    blog_id : int
    body : str

class Picture(BaseModel):
    blog_id : int
    url : str

class Blog(BaseModel):
    user_id:int ####owner of blog
    pic: List[Picture] = []
    comment : List[Comment] = []
    body:str
    class Config():
        orm_mode = True

class ShowUser(BaseModel):
    name:str
    email:str
    blog: List[Blog] = []
    class Config():
        orm_mode = True

class ShowBlog(BaseModel):
    body: str
    user: ShowUser
    pic: List[Picture] = []
    comment : List[Comment] = []
    class Config():
        orm_mode = True

class ShowComment(BaseModel):
    user_id : int
    blog_id : int
    body: str
    class Config():
        orm_mode = True

class ShowPicture(BaseModel):
    blog_id = int
    url : str
    class Config():
        orm_mode = True
        

class Login(BaseModel):
    username: str
    password: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None