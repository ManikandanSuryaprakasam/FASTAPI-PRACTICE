"""Pydantic schemas for request/response validation and serialization.

Defines:
- Article: response schema for an article (title, content, published) with orm_mode=True.
- ArticleBase: request schema for creating/updating articles (title, content, published, creator_id).
- User: nested user schema used inside ArticleDisplay (id, username) with orm_mode=True.
- ArticleDisplay: article response including nested user (title, content, published, user) with orm_mode=True.
- UserBase: request schema for creating/updating users (username, email, password).
- UserDisplay: user response including related articles (username, email, items: List[Article]) with orm_mode=True.

These schemas validate incoming request bodies and serialize SQLAlchemy ORM objects to JSON-friendly responses.
"""


from typing import List
from pydantic import BaseModel    

# Article schemas
class Article(BaseModel):
    title: str
    content: str
    published: bool
    class Config:
        from_attributes = True

class ArticleBase(BaseModel):
    title: str
    content: str
    published: bool
    creator_id:int

#User Inside Article display schema
class User(BaseModel):
    id: int
    username: str
    class Config:
        from_attributes = True

class ArticleDisplay(BaseModel):
    title: str
    content: str
    published: bool
    user: User
    class Config:
        from_attributes = True


# User schemas
class UserBase(BaseModel):
    username: str
    email: str
    password: str

# User display schema with related articles
class UserDisplay(BaseModel):
    username: str
    email: str
    items:List[Article] = []
    class Config:
        from_attributes = True














