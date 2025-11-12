from fastapi import HTTPException,status
from sqlalchemy.orm.session import Session
from db.models import dbUser
from db.hash import Hash
from schemas import UserBase


def create_user(db: Session, request: UserBase):
    new_user = dbUser(
        username=request.username,
        email=request.email, 
        password=Hash.bcrypt(request.password)
        
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_all_users(db: Session):
    users = db.query(dbUser).all()
    return users

def get_user(db: Session, id: int):
    user = db.query(dbUser).filter(dbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    return user

def get_user_by_username(db: Session, username: str):
    user = db.query(dbUser).filter(dbUser.username == username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with username {username} not found")
    return user


def update_user(db: Session, id: int, request: UserBase):
    user = db.query(dbUser).filter(dbUser.id == id)
    if not user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User with id {id} not found")    
    user.update({
        dbUser.username: request.username,
        dbUser.email: request.email,
        dbUser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return 'user updated'

def delete_user(db: Session, id: int):
    user = db.query(dbUser).filter(dbUser.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")   
    db.delete(user)
    db.commit()
    return 'user deleted'