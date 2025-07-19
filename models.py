import requests
from pydantic import BaseModel, confloat, field_validator
import uuid
from datetime import date ,time, timedelta, datetime
from enums import DepartmentEnum
from typing import Literal
#Creating Class for nested attributes
class Module(BaseModel):
    id: int | uuid.UUID
    name: str
    professor: str
    credits: Literal[10,20]   #Credit fields should be only 10 and 20 
    registration_code: str

class Student(BaseModel):
    id: uuid.UUID
    name: str
    date_of_birth: date
    GPA: confloat(ge=0, le=4)   # constraint for GPA between the range 0 and 4
    course: str | None
    department: DepartmentEnum  #union of data types
    fees_paid: bool
    modules: list[Module] = []

    #custom validator for module should be only 3 
    @field_validator('modules')
    def validate_module_length(cls,value):
        if len(value) and len(value) != 3:
            raise ValueError("module should have length 3")
        return value

    @field_validator('date_of_birth')  #cusotm validator 
    def ensure_16_or_over(cls,value):
        sixteen_yr_ago = datetime.now() - timedelta(days=16*365)
        sixteen_yr_ago = sixteen_yr_ago.date()
        if value > sixteen_yr_ago:
            raise ValueError('Too young to enroll ! try next time ')
        return value
        



