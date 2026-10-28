from pydantic import BaseModel  , EmailStr , AnyUrl , Field, field_validator 
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

    @field_validator('email')
    @classmethod 
    def email_validator(cls ,value ): ## cls = for execute other method of this class

        valid_domain = ["hdfc.com" , "icici.com"]

        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError(f"Email domain must be one of {valid_domain}")

        return value 

    @field_validator('name')
    @classmethod 
    def name_validator(cls , value):
        return value.upper()  ## This will convert the name to upper case and return it

    @field_validator("age" , mode = "after")
    @classmethod
    def age_validatoer(cls , value):

        if  0 < value < 100:
            return value
        else:
            raise ValueError("Age must be between 0 and 100")




def insert_patinet_data(patinet : Patient):
    print(patinet.name)
    print(patinet.age)
    print(patinet.alergies)


patinet_info = {"name":"Prasanta" , "age" : 25 ,"email":"abc@hdfc.com" ,"linkdin_url" : "https://www.linkedin.com" ,"weight" : -70.5 , "married" : False ,  "contact_details" : {"email" : "prasanta@example.com" , "number" : "123443443"}}

patinet1 = Patient(**patinet_info)


insert_patinet_data(patinet1)
