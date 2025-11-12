"""Router for user-related endpoints.

Provides:
- APIRouter mounted at prefix "/user" with tag "Users".
- POST "/" -> create_user(request: UserBase, db: Session) returns UserDisplay by calling db_user.create_user.
- GET "/{id}" -> get_user(id: int, db: Session) returns UserDisplay by calling db_user.get_user.
- GET "/" -> get_users(db: Session) returns List[UserDisplay] by calling db_user.get_all_users.
- POST "/{id}/update" -> update_user(id: int, request: UserBase, db: Session) calls db_user.update_user.
- GET "/{id}/delete" -> delete_user(id: int, db: Session) calls db_user.delete_user.
- Uses get_db dependency to provide a SQLAlchemy Session and Pydantic schemas UserBase and UserDisplay for request validation and response serialization.

This docstring describes the routes and how they interact with the database layer.
"""

from typing import List                                                                                
from schemas import UserBase, UserDisplay
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from db.database import get_db
from db import db_user 
from fastapi.params import Depends
from auth.oauth2 import get_current_user
from schemas import UserBase


router = APIRouter(
    prefix="/user",
    tags=['Users']
)


# Create User
@router.post('/', response_model=UserDisplay)
def create_user(request: UserBase, db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.create_user(db, request)

# Read User by ID
@router.get('/{id}', response_model=UserDisplay)
def get_user(id: int, db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.get_user(db, id)


#Read Users
@router.get('/', response_model=List[UserDisplay])
def get_users(db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.get_all_users(db)

# Update User
@router.post('/{id}/update')
def update_user(id: int, request: UserBase, db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.update_user(db, id, request)

# Delete User
@router.get('/{id}/delete')
def delete_user(id: int, db: Session = Depends(get_db),current_user: UserBase = Depends(get_current_user)):
    return db_user.delete_user(db, id)
