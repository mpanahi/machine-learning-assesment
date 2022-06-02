from solution import *
from fastapi import FastAPI

app = FastAPI()
@app.get("/line-up-api")
def get_lineup(name:str):
 event=Event(name)
 return(event.get_lineup())
