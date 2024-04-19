from typing import Union
from fastapi import FastAPI
import requests

app = FastAPI()

item = None

@app.get("/")
def root():
    key = 'duqNoXzM431om35edqH7Qhcrd9M3uYYFm00ZV94K'
    URL = f"https://bigdata.kepco.co.kr/openapi/v1/powerUsage/contractType.do?year=2020&month=11&metroCd=11&cityCd=110&cntrCd=100&apiKey={key}&returnType=json"

    contents = requests.get(URL).text

    return { "message": contents }

@app.get("/name")
def select_name(name: str):
    global item
    if name == item:
        return { "name": item }
    else:
        return { "name": f" {name} name cannot be found"}

@app.post("/name")
def write_name(new_name: str):
    global item
    item = new_name
    return { "name": f"your name {new_name} saved"}

@app.put("/name")
def update_name(updated_name: str):
    global item
    if item:
        item = updated_name
        return { "name": f"name updated into {updated_name} successfully"}
    else:
        return { "name": "name to update do not exist"}

@app.delete("/name")
def delete_name(name: str):
    global item
    if item:
        item = None
        return { "name": "your name deleted successfully"}
    else:
        return { "name": "name cannot be found"}
    