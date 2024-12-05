# Megan Wheeler
# Assignment 8.2
# 4 December 2024

import json

filename = 'student.json'
student_data = []

with open(filename) as sl:
    student_data = json.load(sl)

def FormattedPrint():
    for d in student_data:
        print(f"{d["F_Name"]}, {d["L_Name"]}: ID = {d["Student_ID"]}, Email = {d["Email"]}")

print("This is the original Student list.")
print()
FormattedPrint()

student_data.append({
    "F_Name": "Megan",
    "L_Name": "Wheeler",
    "Student_ID": 46495,
    "Email": "mew@gmail.com"
})

print()
print("This is the updated Student list.")
print()
FormattedPrint()

with open(filename, 'w') as student_file:
    json.dump(student_data, student_file, indent=4, separators=(',',': '))

print()
print("The student.json file was updated.")