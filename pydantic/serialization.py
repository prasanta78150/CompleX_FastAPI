from pydantic import BaseModel 

class Address(BaseModel):
    city :str
    state :str 
    pin : str

class Patinet(BaseModel):
    name:str
    gender:str = "male"
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
    # "gender" : "male",
    "age" :"24" ,
    "address" : address1
}

patinet1 = Patinet(**patient_dict)
## ** with out this pyhton behave entire dictionaty as a positional argument 

## It conver to python to dict format
# patient = patinet1.model_dump()

## It conver Python to json format 
## It give data in string format
# patient = patinet1.model_dump_json()
# print(patient)
# print(type(patient))

## It only expert what i include like "name"
# temp = patinet1.model_dump(include=["name"])


## It print that with out this exclude value 
# temp = patinet1.model_dump(exclude=["name"])
# print(temp)


## exclude unset use when user not want default value in expert in the dataset, 
temp = patinet1.model_dump(exclude_unset= True)
print(temp)