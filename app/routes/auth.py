from fastapi import Body, FastAPI, HTTPException, Response ,status,Depends,APIRouter
from .. import schemas,models,utils
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..databases import get_db
from .. import oath2
from sqlalchemy.orm import Session
route = APIRouter()
@route.post("/login")
def user_login(user_cred : OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)) :

    user = db.query(models.UserModel).filter(models.UserModel.email == user_cred.username).first()
    if not user :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    if not utils.verifyPassword(user_cred.password,user.paswd) :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="User Not Found")
    
    access_token = oath2.create_access_token({"User_id"  : user.id})
    return {"Token" : access_token ,"type" : "bearer"}
