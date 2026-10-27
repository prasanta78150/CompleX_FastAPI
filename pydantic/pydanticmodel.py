from pydantic import BaseModel  , EmailStr , AnyUrl , Field 
from typing import Dict , List , Optional , Annotated 


# type validation 
# data validation
## Field = give meta data attachment and field validation 

class Patient(BaseModel):
    name : str = Annotated[str , Field(max_length = 50 , description = "Name of the Patient" , example = "Prasanta")]
    age : int  = Field(gt = 18 , lt = 100)
    email : EmailStr
    linkdin_url : AnyUrl 
    weight : Annotated[float , Field(gt = 0 , strict = True)]  ## Strict means its value type never chnage 
    married : Annotated[bool , Field(description = "Married or not" , default = False ,example = False)] 
    alergies : Annotated[Optional[List[str]] , Field(description = "Alergies of the Patient", default = None)]       ## This Value is Optional and can be None
    contact_details : Dict[str,str]

def insert_patinet_data(patinet : Patient):
    print(patinet.name)
    print(patinet.age)
    print(patinet.alergies)

def update_patinet_data(patinet : Patient):
    print(patinet.name)
    print(patinet.age)

patinet_info = {"name":"Prasanta" , "age" : 25 ,"email":"abc@gmail.com" ,"linkdin_url" : "https://www.linkedin.com" ,"weight" : -70.5 , "married" : False ,  "contact_details" : {"email" : "prasanta@example.com" , "number" : "123443443"}}


patinet1 = Patient(**patinet_info)

insert_patinet_data(patinet1)
update_patinet_data(patinet1)