from fastapi import FastAPI, Path
from typing import Annotated

# import warnings
# warnings.simplefilter("ignore", DeprecationWarning)

app = FastAPI()

users = {"1": "Имя: Example, возраст: 18"}

@app.get('/')
async def welcome():
    return 'Здравствуйте!Вы на главной странице'

@app.get("/user")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: Annotated[str, Path(min_length=5, max_length=20,  description="Enter username", example="UrbanUser", )]
                      , age: Annotated[int, Path(ge=18, le=90, description="Enter age", example="26")]) -> str:
    current_user = str(int(max(users, key=int)) + 1)
    users[current_user] = f"Имя: {username}, возраст: {age}"
    return f"User {current_user} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: Annotated[int, Path(gt=0, description="Enter user_id")], username: Annotated[
    str, Path(min_length=5, max_length=25, description="Enter username", example="UrbanProfy")]
                      , age: Annotated[int, Path(ge=18, le=90, description="Enter age", example="28")]) -> str:
    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} is updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: Annotated[int, Path(gt=0, description="Enter user_id")]) -> str:
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"

