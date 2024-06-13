from typing import List,Optional

from fastapi import FastAPI
from pydantic import BaseModel,Field

app=FastAPI()

fake_db=[
    {"id":1,"name":"Mark"},
    {"id":2,"name":"Artur"},
    {"id":3,"name":"Kate","vip":[{"id": 1, "type": "gold"}]}]

class Vip(BaseModel):
    id: int
    type: str


class User(BaseModel):
    id: int
    name: str
    vip : Optional[List[Vip]]= None
@app.get("/users/{id}",response_model=List[User])
def hello_my(id: int):
    return [user for user in fake_db if user.get("id")==id]

fake_prod=[{"id":1,"type":"носки","name":"болюза"},
           {"id":2,"type":"штаны","name":"абиб"},
           {"id":3,"type":"кофта","name":"делюк"},
           {"id":4,"type":"шорты","name":"моркс"}]

@app.get("/products")
def get_products(limit:int=1,offset:int=1):
    return fake_prod[offset:][:limit]

fake_db2=[
    {"id":1,"name":"Mark"},
    {"id":2,"name":"Artur"},
    {"id":3,"name":"Kate"}]
@app.post("/users/{user_id}")
def new_name(user_id:int,new_name:str):
    cur_user=list(filter(lambda user: user.get("id")==user_id,fake_db2))
    print(cur_user)
    cur_user[0]["name"]=new_name
    return {"state":200,"data":cur_user}

class Buyer(BaseModel):
    id: int
    name: str
    age: int = Field(ge=0)
@app.post("/buy")
def buy_valid(data:List[Buyer]):
    fake_db2.extend(data)
    return fake_db2