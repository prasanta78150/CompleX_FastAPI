from pydantic import BaseModel  , EmailStr , AnyUrl , Field, field_validator  , model_validator
from typing import Dict , List , Optional , Annotated 


class Patient(BaseModel):
    name : str 
    age : int  
    email : EmailStr
    linkdin_url : AnyUrl 
    weight : float
    married : bool
    alergies : Optional[List[str]] = None     
    contact_details : Dict[str,str] 


    @model_validator(mode = "after") ### model_validator is instance method not a class method 
    def validate_emergency_contact(self): 
        if self.age > 70 and "emergency" not in self.contact_details:
            raise ValueError("Patients older then 60 and emergency contact")
        return self



def inseert_patient_Data(patinet : Patient):
    print(patinet.name)

patinet_info = {"name":"Prasanta" , "age" : 75 ,"email":"abc@gmail.com" ,"linkdin_url" : "https://www.linkedin.com" ,"weight" : -70.5 , "married" : False ,  "contact_details" : {"email" : "prasanta@example.com" , "number" : "123443443"}}

patinet1 = Patient(**patinet_info)

inseert_patient_Data(patinet1)

