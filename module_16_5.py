from fastapi import FastAPI, Path, HTTPException, Request, Body
from fastapi.responses import HTMLResponse
from typing import Annotated
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates

import warnings
warnings.simplefilter("ignore", DeprecationWarning)

app = FastAPI()
templates = Jinja2Templates(directory="Templates")

users = []

class User(BaseModel):
    id: int = None
    username: str
    age: int

@app.get("/", response_class=HTMLResponse)
async def get_all_users(request: Request) -> HTMLResponse:
    return templates.TemplateResponse("users.html", {"request": request, "users": users})

@app.get('/user/{user_id}', response_model=str)
async def get_user(request: Request, user_id: int)-> str:
    try:
        user = next(user for user in users if user.id == user_id)
        return templates.TemplateResponse("users.html", {'request': request, 'user': user})
    except Exception:
        raise HTTPException(status_code=404, detail='User not found')

@app.post("/user/{username}/{age}", response_model=str)
async def post_user(user: User, username: Annotated[str, Path(min_length=3, max_length=24, description="Enter username", example="Elena")],
        age: int = Path(ge=18, le=90, description="Enter age", example=58)) -> str:
    if users:
        current_id = max(user.id for user in users) + 1
    else:
        current_id = 1
    user.id = current_id
    user.username = username
    user.age = age
    users.append(user)
    return f"User {current_id} is registered"


@app.put("/user/{user_id}/{username}/{age}", response_model=str)
async def update_user(user: User, username: Annotated[str, Path(min_length=3, max_length=24, description="Enter username", example="Olga")],
        age: int = Path(ge=18, le=90, description="Enter age", example=59),
        user_id: int = Path(ge=0)) -> str:
    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return f"The user {user_id} is updated."
    raise HTTPException(status_code=404, detail="Пользователь не найден.")
#  uvicorn module_16_5:app --reload


@app.delete('/user/{user_id}', response_model=str)
async def delete_user(user_id: int)-> str:
    id_del = 0
    for delete_user in users:
        if delete_user.id == user_id:
            users.pop(id_del)
            return f'Пользователь {delete_user} успешно удален'
        id_del += 1
    raise HTTPException(status_code=404, detail='User was not found')