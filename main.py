from fastapi import FastAPI
import json

app = FastAPI()

#used to load and read the data
def load_data():  # load_data naam ka function bana rahe hain
    with open("patients.json", "r") as f:  # patients.json file ko read mode me open kar rahe hain
        data = json.load(f)  # JSON file ke data ko Python data me convert kar rahe hain
        return data  # data ko function se return kar rahe hain


@app.get("/")
def hello():
    return{"message":"Patient Managemt System API"}

@app.get("/about")
def about():
    return{"message":"A fully functional API to manage your patient records"}

@app.get("/view")
def view():
    data = load_data()
    return data