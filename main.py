from fastapi import FastAPI  , Path , HTTPException , Query 
from fastapi.responses import JSONResponse
import json
from pydantic import BaseModel , Field , computed_field
from typing import Annotated , Literal

app = FastAPI()

class Patinet(BaseModel):
    id: Annotated[str , Field(... , description="id of the Patient" , examples=["P001"])]
    name : Annotated[str , Field(... , max_length=50 , description="Name of the Parinet")]
    city : Annotated[str , Field(... , max_length= 50 , description= " City of the Patinet")]
    age :  Annotated[int , Field(... , gt=0 ,lt = 120 ,  description= " Age of the patinet")]
    gender : Annotated[Literal['male' , "female" , "others"] , Field(... , description="Gender of the Patinet" , )]
    height :  Annotated[float , Field(... , description="Height of the Patient" )]
    weight :  Annotated[float ,Field(... , description="Weight of the patient")]


    @computed_field
    @property 
    def bmi(self)-> float :
        bmi = round(self.weight / (self.height ** 2), 2)
        return bmi

    @computed_field 
    @property 
    def verdict(self) -> str:

        if self.bmi < 18.5:
            return "underweight"
        elif self.bmi < 25 :
            return "Normal"
        elif self.bi < 30 :
            return "overWeight"
        else:
            return "Obese"



def load_data():
    with open("patients.json" , "r") as f:
        data =  json.load(f)

    return data 

def save_data(data):
    with open("patients.json" , "w") as f:
        json.dump(data, f)

    
@app.get("/")
def hello():
    return {"message" : "Hello Patients!"}

@app.get("/view")
def view_patients():
    data = load_data()

    return data

@app.get("/view/{patient_id}")
def view_patient(patient_id :str = Path(... , description = "the id of the patient to View" , example = "POO1")):
    data = load_data()

    for id in data:
        if id == patient_id:
            return data[patient_id]

    raise HTTPException(status_code = 404 , detail = "Patient not found")

@app.get("/sort")
def sort_patient(sort_by : str = Query(... , description ="Sort on the basis of height , weight , bmi") , 
                 order : str = Query("asc" , description= ("sort in asc or desc order "))):

    valid_fields = ["height" , "weight" , "bmi"]

    if sort_by not in valid_fields:
        raise HTTPException(status_code = 400 , detail = f"Invalid sort field. Valid fields are: {', '.join(valid_fields)}")

    if order not in ["asc" , "desc"]:
        raise HTTPException(status_code = 400 , detail = "Invalid order. Valid orders are: asc, desc")

    data = load_data()

    sort_order = True if order == "desc" else False 

    sorted_data = sorted(data.values() , key = lambda x: x.get(sort_by, 0 ), reverse = sort_order)

    return sorted_data 


@app.post("/create")
def create_patient(patient : Patinet):

    ## Load Data 
    data = load_data()

    ## chekc if the patinet already exist 
    if patient.id  in data:
        raise HTTPException(status_code=400 , detail="Patient is already Exists")

    ## new patinet add that 
    data[patient.id] = patient.model_dump(exclude=("id"))

    #save into the json file
    save_data(data)

    return JSONResponse(status_code = 201 , content = {"message" : "Patinet created succefully"})
