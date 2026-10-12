from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin: str

class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict = {'city':'burewala','state':'Vehari','pin':'1234'}

addreses1 = Address(**address_dict)

patient_dict = {'name':'Jutt','gender':'male','age':34,'address':addreses1}

patient1 = Patient(**patient_dict)

print(patient1)
print(patient1.name)
print(patient1.address.city)
print(patient1.address.pin)


#Benefits

#Better organization of related data (e.g., vitals, addres, insurance)

#Reusability: Use Vitals in multiple models (e.g., Patient, MedicalRecord)

#Readability: Easier for developers and API consumers to understand

#Validation: Nested models are validate automatically-no extra work needed

