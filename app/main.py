from typing import Union

from fastapi import FastAPI

app = FastAPI()

item = ""

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/name/{name}")
def select_name(name: str):
    if name == item:
        return { "name": item }
    else:
        return { "name": f" {name} name cannot be found"}

@app.post("/name/{name}")
def write_name(name: str):
    item = name
    return { "name": f"your name {name} saved"}

@app.put("/name/{name}")
def update_name(name: str):
    if name == item:
        item = name
        return { "name": "name updated successfully"}
    else:
        return { "name": "name cannot be found"}

@app.delete("/name_del/{name}")
def delete_name(name: str):
    if name == item:
        item = ""
        return { "name": "your name deleted"}
    else:
        return { "name": "name cannot be found"}
    