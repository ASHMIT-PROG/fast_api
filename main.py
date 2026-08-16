from fastapi import FastAPI,Path,HTTPException
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

#user want to see a specific patient data 
#for that we will use path parameters

# "Mujhe patient_id URL ke path se chahiye, woh string hona chahiye, required hai, aur API documentation mein uska description aur example bhi dikhao."
@app.get("/patient/{patient_id}")
def view_patient(patient_id:str = Path(..., description="ID of the patient in the DB", example="P001")):# user ko path parameter dena padega ... ka matlab: /patient/P001   

#load all the patient
    data = load_data() 
    if patient_id in data:
        return data[patient_id]# its a library
    raise HTTPException(status_code=404,detail="patient not found")