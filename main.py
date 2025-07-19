import requests
from models import Student, Module
import json
from pprint import pprint

# URL referingcing for basic validation checks 
# url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'

# URL refering to nested validation checks
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

response = requests.get(url)
data = response.json()
# data[-1]['modules'].append({"id":103,"name":"French New Wave Cinema","professor":"Prof. Bailey Stanley","credits":10,"registration_code":"abc"})



"""
for student in data:
    model = Student(**student)
    # print(model.model_dump())
    # print(model)
    excludes = {
        'id' : True,
        'modules' : {'__all__': {'registration_code'}}
    }
    # print(model.model_dump_json(exclude ={'id','module'}))  #instead of mentioning exclude in main class we can mention here as well 
    # pprint(model.model_dump(exclude =excludes))
    #print(json.dumps(Student.model_json_schema(), indent =2))
    pprint(model.department)
    """

for student in data:
    try:
        model = Student(**student)
        print(f"GPA : {model.GPA}, Department: {model.department}")
    except ValueError as e:
        print(f"Error : {e}")
