from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str='Shreyansh'
    age: Optional[int] = None
    grade: int = Field(gt=0, le=100 ,description="Grade must be between 1 and 100")
    email: EmailStr
new_student = { "grade": '90', "email": 'bob@example.com'}
student=Student(**new_student)
student_dict=dict(student)
print(student_dict['name'])

student_json=student.model_dump_json()
