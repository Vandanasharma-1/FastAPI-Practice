from pydantic import BaseModel, EmailStr, AnyUrl, Field
from typing import List, Dict, Optional, Annotated


# step : 1
# class Patient(BaseModel):
#     name : str = Field(max_length=50)
#     email : EmailStr
#     linkedin_url : AnyUrl
#     age : int = Field(gt = 0, lt = 120)
#     weight : float = Field(gt=0)
#     married : bool = False
#     allergies : Optional[List[str]] = Field(max_length = 5)
#     contact_details : Dict[str, str] 


class Patient(BaseModel):
    name : Annotated[str, Field(max_length = 50, 
    title = 'Name of the patient', description = 'Give the name of the patient in less than 50 chars', examples = ['Nistish', 'Amit'])]
    email : EmailStr
    linkedin_url : AnyUrl
    age : int = Field(gt = 0, lt = 120)
    weight : Annotated[float, Field(gt=0, strict = True)]
    married : Annotated[float, Field(default = None, description = 'Is the patient married or not')]
    allergies : Annotated[Optional[list[str]], Field(default = None, max_length = 5)]
    contact_details : Dict[str, str] 


def insert_patients_data(patient = Patient):
    print(patient.name)
    print(patient.age)
    print('Insert into database')


# Step : 2

patient_info = {'name': 'Vandana', 'age' : 30}

patient1 = Patient(**patient_info)

insert_patients_data(patient1)