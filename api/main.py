from fastapi import FastAPI, Depends, HTTPException
from models import User
from typing import List
from db import init_db
from routes.user import router as userrouter
from routes.job import router as jobrouter
from typing import Annotated


app = FastAPI()




@app.on_event("startup")
async def startup():
    await init_db()




app.include_router(userrouter, prefix="/user", tags=["User"])
app.include_router(jobrouter, prefix="/job", tags=["Job"])
