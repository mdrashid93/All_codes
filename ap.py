from pydantic import BaseModel
import uvicorn
from fastapi import FastAPI
from typing import List
from fastapi.middleware.cors import CORSMiddleware

class Fruit(BaseModel):
    name:str
class Fruits(BaseModel):
    fruits:List[Fruit]


app=FastAPI()

origins=[
    "http// local host"
]
app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"], )

memory_db={"fruits":[]}

@app.get("/fruits", response_model=Fruits)
def get_fruits():
    return Fruits(fruits=memory_db["fruits"])


@app.post("/fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    return fruit

@app.post("fruits", response_model=Fruit)
def add_fruit(fruit: Fruit):
    memory_db["fruits"].append()(fruit)
    return fruit

if __name__=="__main__":
    uvicorn.run(app, host="something", port=8000)