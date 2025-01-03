from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Главная страница"}


@app.get("/user/admin")
async def admin():
    return {"message": "Вы вошли как администратор"}


@app.get("/user/{user_id}")
async def user(
        user_id: Annotated[int, Path(ge=1, le=100, title="User ID",
                                     description="Enter User ID", example='1')]):
    return {"message": f'Вы вошли как пользователь № {user_id}'}


@app.get("/user/{username}/{age}")
async def user_age(
        username: Annotated[str, Path(min_length=5, max_length=20, title="Username",
                                      description="Enter Username", example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, title="Age",
                                 description="Enter Age", example='24')]):
    return {"message": f'Информация о пользователе. Имя: {username}, Возраст: {age}'}
