from pydantic import BaseModel  , EmailStr , AnyUrl , Field, field_validator  , model_validator , computed_field
from typing import Dict , List , Optional , Annotated 


class Patient(BaseModel):
    name : str 
    age : int  
    email : EmailStr
    linkdin_url : AnyUrl 
    weight : float
    height: float
    married : bool
    alergies : Optional[List[str]] = None     
    contact_details : Dict[str,str] 

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight / (self.height ** 2),2)
        return bmi



def inseert_patient_Data(patinet : Patient):
    print(patinet.name)
    print(patinet.bmi)

patinet_info = {"name":"Prasanta" , "age" : 75 ,"email":"abc@gmail.com" ,"linkdin_url" : "https://www.linkedin.com" ,"weight" : -70.5 , "height" : 5.5, "married" : False ,  "contact_details" : {"email" : "prasanta@example.com" , "number" : "123443443"}}

patinet1 = Patient(**patinet_info)

inseert_patient_Data(patinet1)

