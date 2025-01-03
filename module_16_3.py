from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/user")
async def Get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def Post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, title="Username",
                                      description="Enter Username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, title="Age",
                                 description="Enter Age", example='24')]) -> str:
    user_id = str(int(max(users, key=int)) + 1)
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'User {user_id} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def Update_user(
        user_id: Annotated[int, Path(ge=1, le=1000, title="Used_id",
                                     description="Enter User_id", example='1')],
        username: Annotated[str, Path(min_length=5, max_length=20, title="Username",
                                      description="Enter Username", example='UrbanProfi')],
        age: Annotated[int, Path(ge=18, le=120, title="Age",
                                 description="Enter Age", example='28')]) -> str:
    users[user_id] = f'Имя: {username}, возраст: {age}'
    return f'The user {user_id} is updated'


@app.delete('/user/{user_id}')
async def Delete_user(
        user_id: Annotated[int, Path(ge=1, le=1000, title="Used_id",
                                     description="Enter User_id", example='1')]) -> str:
    users.pop(str(user_id))
    return f'User {user_id} has been deleted'
