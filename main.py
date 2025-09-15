from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse

app=FastAPI()

db={
    "username":"md_rashid",
    "password":"9347066570"
}

home_html='''
 <!DOCTYPE html>
<html>
<head>
    <title>page title</title>
</head>
<body>
    <h1>Home Page</h1>
    <a href="https://www.youtube.com/watch?v=uk6H-ryc1Wg"> logins</a>
    <a href="/login">login</a>
</body>
</html>
'''
login_html='''
 <!DOCTYPE html>
<html>
<head><title>My page</title></head>
<body>
<a href="/">go home</a>
    <h2>login page</h2>
    <form action="/submit" method="POST"> 
    <div><input type="text" placeholder="email" name="email"></input> </div>
     <div><input type="password" placeholder="password" name="password"></input> </div>
    <button type="submit">login</button>
    </form> 
</body>
</html>
'''
@app.get("/")
def home():
    return HTMLResponse(home_html)

@app.get("/login")
def login():
    return HTMLResponse(login_html)

@app.post("/submit")
def submit(email= Form(...),password=Form(...)):
    if email==db.get("username"):
        if password==db.get("password"):
            return HTMLResponse('''
<h2>Dashboard</h2>you are dancing ''')
        else:
            return HTMLResponse("<p>invalid credential</p>")
    else:
        return HTMLResponse("<p>invalid password</p>")
    


























# # @app.get("/{name}")
# # def home(name):
# @app.get("/")
# def home():
#     # return JSONResponse({"message":" hi, hello"})
    
     
#     # return HTMLResponse(f"<p> hey {name} </p>")

#     # return RedirectResponse("https://www.youtube.com/")
    
#     return HTMLResponse(home_html)

# @app.get("/login")
# def loging():
#     return HTMLResponse(login_html)
