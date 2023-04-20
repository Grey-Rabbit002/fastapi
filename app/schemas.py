from datetime import datetime
from typing import Optional
from pydantic import BaseModel,EmailStr, conint


class ResponseUser(BaseModel) :
    email :EmailStr
    class Config :
        orm_mode = True
        
class Post(BaseModel) :
    title : str
    content : str
    published : bool = True
    owner  : ResponseUser

class CreatePost(Post) :
    pass
class UpdatePost(Post) :
    pass

class ResponsePost(Post) :
    owner_id : int
    class Config :
        orm_mode = True

class CreateUser(BaseModel) :
    email : EmailStr
    paswd : str



class LoginUser(BaseModel) :
    email :EmailStr
    password : str

class Token(BaseModel) :
    access_toke : str
    token_type : str

class TokenData(BaseModel) :
    id : Optional[str]

class Vote (BaseModel):
    post_id : int
    direc : conint(le=1)

class PostOut(BaseModel) :
    post : Post
    Votes : int
    class Config :
        orm_mode = True