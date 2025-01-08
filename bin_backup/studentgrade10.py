student = {
    "name": input("Enter the student's name: "),
    "roll_number": input("Enter the roll number: "),
    "register_number": input("Enter the register number: "),
    "department": input("Enter the department: "),
    "semester": input("Enter the semester: "),
}


student["total_mark"] = int(input("Enter the total mark: "))


if student["total_mark"] >= 90:
    student["grade"] = "A"
elif student["total_mark"] >= 82:
    student["grade"] = "B"
elif student["total_mark"] >= 75:
    student["grade"] = "C"
elif student["total_mark"] >= 60:
    student["grade"] = "D"
elif student["total_mark"] >= 50:
    student["grade"] = "P"
else:
    student["grade"] = "F" 
del student["roll_number"]
print(student)
