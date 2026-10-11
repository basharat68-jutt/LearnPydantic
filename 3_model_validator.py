from pydantic import BaseModel, EmailStr, model_validator
from typing import List, Dict

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @model_validator(mode = 'after')
    def validate_emergency_contact(cls,model):
        if model.age > 60 and 'emergency' not in model.contact_details:
            raise ValueError('Patients older than 60 must have an emergency contact')
        return model


def update_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Ali','email':'abc@hdfc.com','age':'90','weight':75.2,'married':True,'allergies':['polen','dust'],'contact_details':{'phone':'234556','emergency':'938448'}}

patient1 = Patient(**patient_info) #making object for pydantic model

update_patient(patient1)












