import requests
from models import Student, Module
import json

# URL referingcing for basic validation checks 
# url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v1.json'

# URL refering to nested validation checks
url = 'https://raw.githubusercontent.com/bugbytes-io/datasets/master/students_v2.json'

response = requests.get(url)
data = response.json()
# data[-1]['modules'].append({"id":103,"name":"French New Wave Cinema","professor":"Prof. Bailey Stanley","credits":10,"registration_code":"abc"})




# for student in data:
#     model = Student(**student)
#     # print(model.model_dump())
#     # print(model)
#     print(model.model_dump_json())

print(json.dumps(Student.model_json_schema(), indent =2))