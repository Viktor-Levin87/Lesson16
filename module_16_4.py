from fastapi import FastAPI, Path, HTTPException
from typing import Annotated, List
from pydantic import BaseModel, Field

users = []


class User(BaseModel):
    id: int
    username: str = Field(..., min_length=5, max_length=20, description="Enter Username")
    age: int = Field(..., ge=18, le=120, title="Age", description="Enter Age")


app = FastAPI()


@app.get("/user")
async def Get_users() -> List[User]:
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def Post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, title="Username",
                                      description="Enter Username", example='UrbanProfi')],
        age: Annotated[int, Path(ge=18, le=120, title="Age",
                                 description="Enter Age", example='28')]):
    new_id = max((u.id for u in users), default=0) + 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def Update_user(
        user_id: Annotated[int, Path(ge=1, le=1000, title="Used_id",
                                     description="Enter User_id", example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, title="Username",
                                      description="Enter Username", example='UrbanProfi')],
        age: Annotated[int, Path(ge=18, le=120, title="Age",
                                 description="Enter Age", example='28')]):
    for u in users:
        if u.id == user_id:
            u.username = username
            u.age = age
            return u
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def Delete_user(
        user_id: Annotated[int, Path(ge=1, le=1000, title="Used_id",
                                     description="Enter User_id", example='1')]):
    for i, u in enumerate(users):
        if u.id == user_id:
            del users[i]
            return u
    raise HTTPException(status_code=404, detail="User was not found")
