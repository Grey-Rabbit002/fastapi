from fastapi import Depends, HTTPException,status
from jose import jwt,JWTError
from datetime import datetime,timedelta
from . import schemas
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .import databases
from . import models
from . config import setting
oath2_scheme = OAuth2PasswordBearer('login')
ALGORITHM = str(setting.algorithm)
SECRET_KEY = str(setting.secret_key)
EXPIRE_TIME = int(setting.access_token_expire_minutes)
def create_access_token(data : dict) :
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRE_TIME)
    to_encode.update({"expire" : str(expire)})
    encoded_token = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_token

def verify_token(token:str,cred_excep) :
    try :
        payload = jwt.decode(token,SECRET_KEY,[ALGORITHM])
        id = str(payload.get("User_id"))
        if id is None :
            raise cred_excep
        token_data = schemas.TokenData(id=id)
    except JWTError :
        raise cred_excep
    return token_data

def current_user(token :str = Depends(oath2_scheme),db : Session = Depends(databases.get_db)) :
    cred_excep = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User Credentials are Invalid",headers={"WWW-Authenticate" : "Bearer"})
    token = verify_token(token=token,cred_excep=cred_excep)
    user = db.query(models.UserModel).filter(models.UserModel.id == token.id).first()
    return user