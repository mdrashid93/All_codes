from fastapi import FastAPI,HTTPException
from fastapi.responses import JSONResponse
import sqlite3



app=FastAPI()

def get_db():
    conn=sqlite3.connect('database100')
    return conn

@app.get("/")
def home(name):
    return "hello"+name


@app.post("/users")
def create_user(name,username,password,course_id):
    course_id=int(course_id)
    try:
        conn=get_db() 
        cursor=conn.cursor()    
        cursor.execute("INSERT INTO users(name,username,password,course_id) VALUES(?,?,?,?)",(name,username,password,course_id))
        user_id=cursor.lastrowid
        conn.commit()
        conn.close()
        return JSONResponse(content={
            "message":"successfully created user",
            "user_id":user_id
        })
    except Exception as e:
        print("something went wrong")
        
@app.get("/users")
def get_all_users():
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM users")
    users=cursor.fetchall()
    conn.close()
    result=[]
    for user in users:
        result.append(list(user))
    return JSONResponse(result)   

@app.put("/users/{user_id}")
def update_user_password(user_id,password):
    Conn=get_db()
    cursor=Conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id=?",(user_id,))
    if not cursor.fetchone():
        Conn.close()
        return JSONResponse(content={
            "message":"user with id-{user_id}was not found "
        })
    if password:
        cursor.execute("UPDATE users SET password=? WHERE id=?",(password,user_id))
        Conn.commit()
        Conn.close()
        return JSONResponse(content={
            "message":"updated successfuly for user-{user_id}"
            
        })
        
@app.delete("/users/{user_id}")
def delete_user(user_id):
    conn=get_db()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM users WHERE id=?",(user_id,))
    if cursor.rowcount==0:
        raise HTTPException(status_code=404,detail="user not found to delete")
    conn.commit()
    conn.close()
    return JSONResponse({
        "message":"successfully delted user-{user_id}"
    })
        






























# from fastapi import Body, FastAPI
# import json
# app=FastAPI()


# @app.get("/g/{age}")
# def home(name,age):
#     data={"appnAME":f"{name}-{age}"}
#     return data


# @app.get("/g")
# def add(first:int,second:int):
   
#     return {"result":first+second}


# @app.get("/{id }")#path parameter
# def home(name,id):
#     return id

# @app.post("/data")
# def greet(details: dict= Body(...)):
#     return f"Hello {details["username"]}"

# users_database={
#     # "md":"raas",
#     # "pa":"papa12"
#     }

# DB_FILE="database.json"

# def load_json_db():
#     #open file and return data
#     with open("database.json","r") as f:
#         return json.load(f)

# def save_json_db(user_details):
#     with open("databse.json","w") as f:
#         json.dump(user_details)
    
    
#     # @app.post("/data")
# # def greeting(details:dict=Body(...)):
# #     users_database.update({details.get("username"): details.get("password")})
# #     return users_database


# @app.post("/save")
# def user(details:dict=Body(...)):
#     all_users=load_json_db()
#     all_users.append({details.get("username"): details.get("password")})
#     print(all_users)
#     # save_json_db(all_users )
#     all_users=load_json_db()
#     return users_database








# # from fastapi import Body,FastAPI
# # import json
# # app=FastAPI()
# # def load_jsondb():
# #     with open("database.jsm,"r"")as f:
# #         return json.load(f)
# # def save_kjspm(userdetails):
# #     with open("databse.jspn","w")as f:
# #         json.dump(userdetails,f)

# # @app.post("/save")
# # def users(detials:dict=Body(...)):
# #     all_users=load_json_db()
# #     all_users.append({detials.get("username"),detials.get("password")})
# #     save_json_db(all_users)
# #     all_users=load_json_db()
# #     return all_users