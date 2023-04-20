from fastapi import FastAPI
from .routes import user,post,auth,vote
from .databases import engine
from . import models
from fastapi.middleware.cors import CORSMiddleware
# models.Base.metadata.create_all(bind = engine)
app = FastAPI()
origins = [ "*"
           ]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def pri() :
    return {"hello" :"world"}

app.include_router(post.route)
app.include_router(user.route)
app.include_router(auth.route)
app.include_router(vote.route)



