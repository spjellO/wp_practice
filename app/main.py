from typing import Union

from fastapi import FastAPI

app = FastAPI()

global item

@app.get("/")
def read_root():
    return {"Hello": "World"}


'''@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}'''

@app.post("/name/{name}")
def insert(name: str):
    item = name
    return {"message": f"your name {item} has been saved"}

@app.get("/namelist/{name}")
def select(name: str):
    if item == name:
        return {"message" : "name that you've saved is" + name}
    else :
        return {"message" : "name cannot be found"}