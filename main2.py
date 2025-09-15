from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse, HTMLResponse, RedirectResponse

app=FastAPI()

db={
    "username":"md_rashid",
    "password":"9347066570"
}

a_html='''
 <!DOCTYPE html>
<html>
<head>
    <title>page title</title>
    
    
</head>
<body>
<div class="accordion" id="accordionExample">
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
        Accordion Item #1
      </button>
    </h2>
    <div id="collapseOne" class="accordion-collapse collapse show" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the first item’s accordion body.</strong> It is shown by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It’s also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
        Accordion Item #2
      </button>
    </h2>
    <div id="collapseTwo" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the second item’s accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It’s also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
      </div>
    </div>
  </div>
  <div class="accordion-item">
    <h2 class="accordion-header">
      <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapseThree" aria-expanded="false" aria-controls="collapseThree">
        Accordion Item #3
      </button>
    </h2>
    <div id="collapseThree" class="accordion-collapse collapse" data-bs-parent="#accordionExample">
      <div class="accordion-body">
        <strong>This is the third item’s accordion body.</strong> It is hidden by default, until the collapse plugin adds the appropriate classes that we use to style each element. These classes control the overall appearance, as well as the showing and hiding via CSS transitions. You can modify any of this with custom CSS or overriding our default variables. It’s also worth noting that just about any HTML can go within the <code>.accordion-body</code>, though the transition does limit overflow.
      </div>
    </div>
  </div>
</div>
    <h1>Home Page</h1>
    <a href="https://www.youtube.com/watch?v=uk6H-ryc1Wg">youtube</a>
    <a href="/login">login</a>
    <a href="/home">home</a>
    <a href="/contact">contact</a>
    <a href="/about">about</a> 

</body>
</html>
'''

login_html='''
 <!DOCTYPE html>
<html>
<head><title>My page</title></head>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-sRIl4kxILFvY47J16cr9ZwB07vP4J8+LH7qKQnuqkuIAvNWLzeN8tE5YBujZqJLB" crossorigin="anonymous">
<body>
<nav class="navbar navbar-expand-lg bg-body-tertiary">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNav">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item">
          <a class="nav-link disabled" aria-disabled="true">Disabled</a>
        </li>
      </ul>
    </div>
  </div>
</nav>
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
about_html=''' <!DOCTYPE html>
<html>
<head>
    <title>page title</title>
</head>
<body>
<h3> welcome </h3>

</body>
</html>

'''
contact_html=''' <!DOCTYPE html>
<html>
<head>
    <title>page title</title>
</head>
<body>
<h3>9347066570</h3>
<h4>md.rasshid9@gmail.com</h4>

</body>
</html>

'''


@app.get("/")
def a():
    return HTMLResponse(a)

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
    
@app.get("/about")
def about():
  return HTMLResponse(about_html)

@app.get("/contact")
def contact():
  return HTMLResponse(contact_html)
    
    