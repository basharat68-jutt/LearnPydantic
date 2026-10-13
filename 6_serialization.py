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

temp = patient1.model_dump(exclude={'name'}) #existing pydantic model ko dictionary mein convert kr dy ga

print(temp)
print(type(temp))