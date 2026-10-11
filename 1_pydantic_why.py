from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: Annotated[str, Field(max_length=50, title='Name of the patient', description='Give the name of the patient in less than 50 characters', examples=['Nitesh','Amit'])]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0,lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool,Field(default=None, description='Is the patient Married or Not?')]
    allergies: Annotated[Optional[List[str]], Field(default=None,max_length=5)] #every item will be string
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

patient_info = {'name':'nitish','email':'abc@gmail.com','linkedin_url':'http://linkedin.com','age':30,'weight':90,'married':True,'contact_details':{'phone':'23445'}}

patient1 = Patient(**patient_info)
insert_patient_data(patient1)