from typing import Union

from fastapi import FastAPI

app = FastAPI()

class item():
    name = ""

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name_wr/{name}")
def select_name(name: item):
    if name is item.name:
        return { "name": name }
    else:
        return { "name": "name cannot be found"}

@app.post("/name_sel/{name}")
def write_name(name: item):
    item.name = name
    return { "name": "your name saved"}

@app.put("/name_up/{name}")
def update_name(name: item):
    if name is item.name:
        item.name = name
    else:
        return { "name": "name cannot be found"}

@app.delete("/name_del/{name}")
def delete_name(name: item):
    if name is item.name:
        item.name = ""
        return { "name": "your name deleted"}
    else:
        return { "name": "name cannot be found"}
    