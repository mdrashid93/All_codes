# form fastapi import fastAPI

# app=fastAPI()

# @app.get("/predict")
# def predict_model(age:int,sex:str):
#     if age<15 or sex=="f":
#         return {"survived":1}
#     else:
#         return{"survived":0}
    
    
    
form fastapi import FastAPI

app=FastAPI()

@app.get("/"):
async def root():
    return{"message":"hi baby"}
@app.get("/name/{name}")
async def say_hello(name:str):
    return {"message":f"hello{name}"}

    