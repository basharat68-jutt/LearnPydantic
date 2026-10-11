from pydantic import BaseModel
from typing import List, Dict, Optional

class Patient(BaseModel):

    name: str
    age: int
    weight: float
    married: bool
    allergies: Optional[List[str]] = None #every item will be string
    contact_details: Dict[str,str] #key and values both will be str


def insert_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print("Inserted")

def update_patient_data(patient:Patient):

    print(patient.name)
    print(patient.age)
    print("Updated")

patient_info = {'name':'nitish','age':30,'weight':90,'married':True,'contact_details':{'email': 'abc@gmail.com','phone':'23445'}}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)