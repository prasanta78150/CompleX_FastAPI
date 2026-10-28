from pydantic import BaseModel 

class Address(BaseModel):
    city :str
    state :str 
    pin : str

class Patinet(BaseModel):
    name:str
    gender:str
    age:str 
    address : Address 


address_dict = {
    "city" : "BBSR",
    "state" : "Odisha",
    "pin" : "657172"
}


address1 = Address(**address_dict)

patient_dict = {
    "name" :"Prasanta",
    "gender" : "male",
    "age" :"24" ,
    "address" : address1
}

patinet1 = Patinet(**patient_dict)
## ** with out this pyhton behave entire dictionaty as a positional argument 

def Patinet_details(patinet : Patinet):
    print(patinet.name)


Patinet_details(patinet1)

## Beter organisation of related data 
## Reusability : Use vitals in multiple models 

## Readiablity : Easier for devlopers and API consumers to understand 

## Validation :Nested models are validated automaticaly - no extra work needed 

