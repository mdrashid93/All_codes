from fastapi import FastAPI
from fastapi.responses import HTMLResponse, RedirectResponse,JSONResponse
from src.routes.auth import router


app=FastAPI()


# @app.get('/')
# def hello():
#     # return HTMLResponse('''
#     #                     <h1>hello<h1>
#     #                     ''')
#     # return JSONResponse({
#     #     "message":"hello"
#     # }) 
#     return RedirectResponse("https://medhaedutech.com")


app.include_router(router)