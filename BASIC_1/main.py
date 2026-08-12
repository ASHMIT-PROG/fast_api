from fastapi import FastAPI
app = FastAPI()
#making an endpoint 
#/ is the route 
@app.get("/")
def hello():
    return{'message':'hello world'}
#/about is the route 
#get is tge http method 
@app.get("/about")
def about():
    return{
        'message':'this is the second end point that u can learn ai'
    }
