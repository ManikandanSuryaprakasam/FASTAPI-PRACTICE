"""Router for article-related endpoints.

Provides:
- APIRouter mounted at prefix "/article" with tag "article".
- POST "/" -> create_article(request: ArticleBase, db: Session) returns ArticleDisplay by calling db_article.create_article.
- GET "/{id}" -> get_article(id: int, db: Session) returns ArticleDisplay by calling db_article.get_article.
- Uses get_db dependency to provide a SQLAlchemy Session and Pydantic schemas ArticleBase and ArticleDisplay for request/response validation.
"""


from typing import List                                                                                
from schemas import ArticleBase, ArticleDisplay, UserBase
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from db.database import get_db
from db import db_article 
from auth.oauth2 import get_current_user


router = APIRouter(
    prefix="/article",
    tags=['article']
)


#Create Article
@router.post('/', response_model=ArticleDisplay)
def create_article(request: ArticleBase, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    return db_article.create_article(db, request)   

#Get article by ID
@router.get('/{id}', response_model=ArticleDisplay)
def get_article(id: int, db: Session = Depends(get_db), current_user: UserBase = Depends(get_current_user)):
    
    return db_article.get_article(db, id)
    '''return{
      'data': db_article.get_article(db, id),
      'current_user': current_user
    }'''