from fastapi import FastAPI
from pydantic import BaseModel

class input(BaseModel):
    age:int
    sex:str
app=FastAPI()
@app.get("/predict")
def predict_model(d:input):
    if d.age<10 or d.sex=="f":
        return {"survived":1}
    else: 
        return {"survied":0}