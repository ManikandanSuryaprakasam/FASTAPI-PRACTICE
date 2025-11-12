from fastapi import APIRouter,status,Response
from enum import Enum
from typing import Optional

from fastapi.params import Depends
from auth.oauth2 import get_current_user
from schemas import UserBase

router = APIRouter(
    prefix="/blog",
    tags = ['blog']
)


@router.get('/all', 
         tags=['blog'], 
         summary="Retrieve all blogs", 
         description="This api call simulates fetching all blogs")
def get_blog_all(page = 1,page_size: Optional[int] = None):
    return {'message': f'All {page_size} blogs on page {page}'}

@router.get('/{id}/comments/{comment_id}',tags=['blog','comments'])
def get_comment(id:int, comment_id: int, valid: bool = True, username: Optional[str] = None):
    """ 
    Simulates fetching comments of a blog

    - **id:** mandatory path parameter
    - **comment_id:** mandatory path parameter
    - **valid:** optional query parameter
    - **username:** optional query parameter
    """
    return {'message': f'Blog ID is {id}, comment ID is {comment_id}, valid is {valid}, username is {username}'}

class BlogType(str, Enum):
    short = 'short'
    story = 'story'
    howto = 'howto'

@router.get('/type/{btype}')
def get_blog_type(btype: BlogType,current_user: UserBase = Depends(get_current_user)):
    return {'message': f'Blog type {btype.value}'}

@router.get('/{id}',status_code=status.HTTP_200_OK)
def get_blog(id:int,response:Response,current_user: UserBase = Depends(get_current_user)):
    if id > 5:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'error': 'Blog not found'}
    else:
        response.status_code = status.HTTP_200_OK
        return {'message': f'Blog ID is {id}'}


    





