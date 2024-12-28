from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {"message": "Здравствуйте!Вы на главной странице"}

@app.get("/user/admin")
async def adm() -> dict:
    return {"message": "Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def id_adress(user_id:str) -> dict:
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.get("/user/{user_name}/{age}")
async def inf_user(user_name:str, age: str) -> dict:
    return {"message": f"Информация о пользователе. Имя: {user_name}, Возраст: {age}"}