from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):

    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str,str]

    @field_validator('email') #On which we want apply this Function
    #field_validator is a class method
    @classmethod #Method that we are creating this is a class method it tells Python that this is a class Method
    def email_validator(cls, value):  #cls is class and value is value of Email

        valid_domains = ['hdfc.com','icii.com']
        #abc@gmail.com
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')

            return value

    @field_validator('name')
    @classmethod

    def transformer_name(cls,value):
        return value.upper()


def update_patient(patient: Patient):

    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')

patient_info = {'name':'Ali','email':'abc@hdfc.com','age':'30','weight':75.2,'married':True,'allergies':['polen','dust'],'contact_details':{'phone':'234556'}}

patient1 = Patient(**patient_info)

update_patient(patient1)










