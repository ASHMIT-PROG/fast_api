#1 product management api 
from fastapi import FastAPI
import json

app = FastAPI()

#to load the data of the json
def load_data():
    with open("products.json","r") as f:
        data = json.load(f)
        return data

@app.get("/")
def hello():
    return{
        "message":"welcome to the page"
    }

@app.get("/about")
def about_page():
    return{
        "message":"this is just a test to get all the details of the product"
    }

@app.get("/show")
def show():
    products = load_data()
    return products