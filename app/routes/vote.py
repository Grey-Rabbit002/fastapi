from fastapi import HTTPException, Response ,status,Depends,APIRouter
from sqlalchemy.orm import Session
from ..databases import get_db
from .. import oath2,schemas,databases,models
route = APIRouter()

@route.post("/vote",status_code=status.HTTP_201_CREATED)
async def vote(vote : schemas.Vote,db:Session = Depends(databases.get_db),curr_user :int= Depends(oath2.current_user)) :

    post = db.query(models.PostModel).filter(models.PostModel.id == vote.post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Post with id: {vote.post_id} does not exist")

    vote_query = db.query(models.Vote).filter(models.Vote.post_id== vote.post_id,models.Vote.post_id == curr_user.id)
    found_vote = vote_query.first()
    if vote.direc == 1 :
        if found_vote :
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="already found")
        new_vote = models.Vote(post_id = vote.post_id,user_id = curr_user.id)
        db.add(new_vote)
        db.commit()
        return {"message" : "Voted Successfully"}
    else:
        if not found_vote :
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="not found")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return {"message ": "Downvoted Successfully"}