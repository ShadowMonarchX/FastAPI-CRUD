from os import error
from turtle import up
from fastapi import FastAPI # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List 


app = FastAPI()

class Tea(BaseModel) :
    id : int
    name : str 
    origin : str

teas : List[Tea] = []

print("Jenish")
@app.get("/")
def read_root():
    return {"Hello JR Shekhada"}

@app.get("/test")
def get_test() :
    return teas

@app.post("/teas")
def add_test(t1 : Tea) :
    teas.append(t1)
    return t1

@app.put("/teas/{tea_id}")
def update_tea(tea_id:int,updated_tea:Tea) :
    for i , tea in enumerate(teas) :
        if tea.id == tea_id :
            teas[i] = update_tea
            return update_tea
    return {"error" : "Tea not Found"}

@app.delete("teas/{tea_id}")
def delete_tea(tea_id:int) :
    for i , tea in enumerate(teas) :
        if tea.id == tea_id :
            deleted = teas.pop(i)
            return deleted
    return {"error" : "tea is not found " }


