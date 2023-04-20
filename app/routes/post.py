from fastapi import HTTPException, Response ,status,Depends,APIRouter
from typing import List,Optional
from .. import schemas,models,utils
from sqlalchemy.orm import Session
from ..databases import get_db
from .. import oath2
from sqlalchemy import func, text

route = APIRouter()
@ route.get("/posts/show",)
def posts(db:Session = Depends(get_db),cur_user = Depends(oath2.current_user),limit : int = 10,skip : int = 0,search : Optional[str] = "") :
    results = db.query(models.PostModel, func.count(models.Vote.post_id).label("votes")).join(
        models.Vote, models.Vote.post_id == models.PostModel.id, isouter=True).group_by(models.PostModel.id).filter(models.PostModel.title.contains(search)).limit(limit).offset(skip).all()
    if not results :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="No Post Found")
    # cursor.execute("""select * from posts""")
    # posts = cursor.fetchall()
    # print(posts)
    # return {"posts" : my_post}
    # print(cur_user.email)
    return list(dict(results))

@ route.post("/posts/create",status_code=status.HTTP_201_CREATED,response_model=schemas.ResponsePost)        
async def  createpost(new_post : schemas.CreatePost,db:Session = Depends(get_db),cur_user = Depends(oath2.current_user)) :
    # async def create( payload: dict = Body(...)) :
    #     print(payload)
    #     # return {"msg" : "successfully created a post"}
    #     return {"post" :f"title :{payload['title']}"}
    # def findPost(id) :
    #     for idx in my_post :
    #         if idx['id'] == id :
    #             return idx

    # print("The title of posts is        ->" ,new_post.title)
    # print("The content  of posts is     ->" ,new_post.content)
    # print("The publication of posts is  ->" ,new_post.published)
    # print("The rating of posts is       ->" ,new_post.rating)
    # post_dict = new_post.dict()
    # post_dict['id'] = randrange(0,1000000)
    # my_post.append(post_dict)
    # cursor.execute("""insert into posts(title,content,published) values(%s,%s,%s) returning *""",(new_post.title,new_post.content,new_post.published))
    # post = cursor.fetchone()
    # connection.commit()
    # post = models.PostModel(title = new_post.title,content = new_post.content,published = new_post.published)
    new_post = models.PostModel(owner_id = cur_user.id,**new_post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

@route.get ("/posts/Specificposts/{id}",response_model=schemas.ResponsePost)
async def get_specific(id : str, response : Response,db:Session = Depends(get_db),cur_user = Depends(oath2.current_user)) :
    # post = findPost(int(id))
    # if not post :
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id {id} not found")
    #     # response.status_code = status.HTTP_404_NOT_FOUND
    #     # return {"specific_post" : "Post Not Exists"}
    # return{"Specific_Post" : post}
    # cursor.execute("""select * from posts where id = %s """,(str(id),))
    # post = cursor.fetchone()
    post = db.query(models.PostModel).filter(models.PostModel.id == id).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return post

@ route.delete ("/deleteposts/{id}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id:str,db:Session = Depends(get_db),cur_user = Depends(oath2.current_user)):
    #def find_index_post(id) :
    #     for idx,post in enumerate(my_post) :
    #         if post['id'] == id :
    #             return idx

    # index = find_index_post(id)
    # if index is None :
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Does Not Exists")
    # my_post.pop(index)
    # cursor.execute("""delete from posts where id = %s returning *""",(str(id),))
    # deleted_post = cursor.fetchone()
    # connection.commit()
    # print(deleted_post)
    deleted_post = db.query(models.PostModel).filter(models.PostModel.id == id)
    if deleted_post.first() is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post Not Found")
    if deleted_post.first().owner_id != cur_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Unauthorised operation")
    deleted_post.delete(synchronize_session=  False)
    db.commit()
    # return {"message" : "Post was successfully deleted"}
    return {Response(status_code=status.HTTP_204_NO_CONTENT)}
        
@route.put ("/posts/update/{id}",response_model=schemas.ResponsePost)
async def update_post(id :int, updated_post : schemas.UpdatePost,db:Session = Depends(get_db),cur_user = Depends(oath2.current_user)) :
    # index = find_index_post(id)
    # if index is None :
    #     raise HTTPException(status_code = status.HTTP_404_NOT_FOUND)
    
    # post_dict = post.dict()
    # post_dict['id'] = id
    # my_post[index] = post_dict
    # cursor.execute(""" update posts set title = %s , content = %s where id = %s returning *""",(post.title,post.content,id))
    # updated_post = cursor.fetchone()
    # connection.commit()
    post = db.query(models.PostModel).filter(models.PostModel.id == id)
    if  post.first() is None :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Post not found")
    if   post.first().owner_id != cur_user.id :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Unauthorised operation")
    post.update(updated_post.dict(),synchronize_session=False)
    db.commit()
    return post.first()


