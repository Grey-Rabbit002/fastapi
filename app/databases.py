from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
from . config import setting
SQLALCHEMY_DATABASE_URL = f'postgresql://{setting.database_username}:{setting.database_password}@{setting.database_hostname}:{setting.database_port}/{setting.database_name}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)
sesionLocal = sessionmaker(autoflush=False,bind=engine,expire_on_commit=False)
Base = declarative_base()

def get_db():
    db = sesionLocal()
    try :
        yield db
    finally:
        db.close()



# while True:
#     try :
#         connection = psycopg2.connect(host = "localhost",cursor_factory=RealDictCursor,user = "postgres", password = "Arjun2002###",database = "postgres")
#         cursor  = connection.cursor()
#         print("Databse Connected Successfully")
#         break
#     except Exception as error :
#         print("Could Not Connect")

            # my_post = [
            #             {'title' :'Food','content':'I like Pizza','id':1},
            #             {'title' :'Tech','content':'I like Flutter','id':2},
            #          ]
