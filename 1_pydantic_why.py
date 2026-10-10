from pydantic import BaseModel
from typing import List, Dict

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: List[str] #every item will be string
    contact_detail: Dict[str,str] #key and values both will be str


def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("Inserted")

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {'name':'nitish','age':30,'weight':90,'married':True,'allergies':['pollen','dust'],'contact_details':{'email': 'abc@gmail.com','phone':'23445'}}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)