import numpy as np
from copy import deepcopy

def student_status(avg_grade):
    if avg_grade >= 17:
        status = 'Great'
    elif avg_grade >= 12:
        status = 'Normal'
    elif avg_grade >= 0:
        status = 'Fail'
    return status

students_information = list()
student = {}
for m in range(3):
    print(f"Enter student {m+1}")
    student['first_name'] = input("Enter first name: ")
    student['last_name'] = input("Enter last name: ")
    grades = input("Enter grades separated with comma: ")
    grades = grades.split(',')
    student['grades'] = [int(grade) for grade in grades]
    students_information.append(deepcopy(student))

for student in students_information:
    grades = student['grades']
    sum_grade = sum(grades)
    avg_grade = sum_grade / len(grades)
    print(f"Status of {student['first_name']} {student['last_name']} is {student_status(avg_grade)}")


