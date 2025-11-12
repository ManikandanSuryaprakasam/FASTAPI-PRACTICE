from fastapi import APIRouter, Body, Query,Path
from pydantic import BaseModel
from typing import Dict, Optional,List
from fastapi.params import Depends
from auth.oauth2 import get_current_user
from schemas import UserBase

router= APIRouter(
    prefix="/blog",
    tags=['blog']
)

class Image(BaseModel):
    url: str
    alias: str

class BlogPost(BaseModel):
    title: str
    content: str
    nbcomments: str
    published: Optional[bool] = True
    tags:List[str]=[]
    metadata: Dict[str, str] = {'key1': 'val1'}
    image: Optional[Image] = None
    
@router.post('/new/{id}')
def create_blog(blog_post: BlogPost, id: int, version: int = 1,current_user: UserBase = Depends(get_current_user)):
    return {
        'id': id,
        'data': blog_post,
        'version': version
    }

@router.post('/new/{id}/comment/{comment_id}')
def create_comment(blog: BlogPost, id: int, 
                comment_title: str = Query(None, 
                title="Comment Title", 
                description="The title of the comment created", 
                alias="commenttitle",
                deprecated=True
                ),
                content:str = Body(...,
                                   min_length=10,
                                   max_length=50,
                                   pattern="^[a-z]*$"
                                   ),
                v: Optional[list[str]] = Query(['1.0', '1.1', '2.0']) ,
                comment_id: int = Path(..., gt=5, le=10),current_user: UserBase = Depends(get_current_user)
        ):
    return {
        'blog': blog,
        'id': id,
        'comment_title': comment_title,
        'content': content,
        'version': v,
        'comment_id': comment_id
   
    }
