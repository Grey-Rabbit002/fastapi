from sqlalchemy import TEXT, TIMESTAMP, Integer,Boolean,String,Column,ForeignKey
from sqlalchemy.sql.expression import null 
from .databases import Base
from sqlalchemy.orm import relationship
class PostModel(Base):
    __tablename__ = "postable"
    id = Column(Integer,primary_key=True,nullable=False)
    title = Column(String,nullable=False)
    content = Column(String,nullable=False)
    published = Column(Boolean,server_default='True')
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=str('now()'))
    owner_id = Column(Integer,ForeignKey("usertable.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("UserModel")

class UserModel(Base) :
    __tablename__ = "usertable"
    id = Column(Integer,primary_key=True,nullable=False)
    email = Column(String,nullable=False,unique=True)
    paswd = Column(String,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=str('now()'))



class Vote(Base) :
    __tablename__ = "vote"
    user_id = Column(Integer,ForeignKey("usertable.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("postable.id",ondelete="CASCADE"),primary_key=True)
    