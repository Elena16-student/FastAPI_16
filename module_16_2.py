from fastapi import FastAPI, Path
from typing import Annotated

import warnings
warnings.simplefilter("ignore", DeprecationWarning)

app=FastAPI()

@app.get('/')
async def welcome():
    return 'Здравствуйте!Вы на главной странице'

@app.get('/user/admin')
async def adm():
    return 'Вы вошли как администратор'

@app.get('/user/{user_id}')
async def id_adress(user_id: Annotated[int,Path(ge=1, le=130, description='Enter User ID', example='11')]):
    return f'Вы вошли как пользователь № {user_id}'

@app.get('/user/{username}/{age}')
async def inf_user(username: Annotated[str,Path(min_length=3, max_length=28,
                                      description='Enter username', example='UrbanStudent')],
                    age: Annotated[int,Path(ge=18, le=90, description='Enter age', example='24')]):
    return f'Информация о пользователе. Имя: {username}, Возраст: {age}'
#uvicorn module_16_2:app --reload