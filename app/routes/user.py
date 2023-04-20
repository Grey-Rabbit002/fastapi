from fastapi import HTTPException, Response ,status,Depends,APIRouter
from typing import List
from .. import schemas,models,utils
from sqlalchemy.orm import Session
from ..databases import get_db

route = APIRouter(prefix="/users",tags=['Users'])

@route.post ("/",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponseUser)
async def create_user(new_user : schemas.CreateUser,db : Session = Depends(get_db)) :
    user = models.UserModel(**new_user.dict())
    hashed_pswd = utils.hash(new_user.paswd)
    user.paswd  = hashed_pswd
    # check = db.query(models.UserModel).filter(models.UserModel.email).first()
    # print(check)
    # print(new_user.email)
    # if check == new_user.email :
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Email Already Taken")
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

@route.get("/{id}",response_model = schemas.ResponseUser)
def get_user(id:int,db : Session = Depends(get_db)) :
    user = db.query(models.UserModel).filter(models.UserModel.id == id).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User not found")
    return user
        