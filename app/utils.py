from passlib.context import CryptContext
pswd_context = CryptContext(schemes=['sha256_crypt'])


def hash(password:str) :
    return pswd_context.hash(password)

def verifyPassword(plain_password,hashed_password) :
    print(pswd_context.hash(plain_password))
    print(hashed_password)
    return pswd_context.verify(plain_password,hashed_password)