from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @computed_field
    @property
    def bmi(self) -> float:
        bmi = round(self.weight /(self.height**2),2)
        return bmi




def update_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI',patient.bmi)
    print('updated')

patient_info = {'name':'Ali','email':'abc@hdfc.com','age':'30','weight':75.2,'height':1.52,'married':True,'allergies':['polen','dust'],'contact_details':{'phone':'234556'}}

patient1 = Patient(**patient_info) #making object for pydantic model

update_patient(patient1)