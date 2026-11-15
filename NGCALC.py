print("<<<<STUDENT MANAGEMENT SYSTEM>>>>")

Name = input("enter student name:")
rollno = input("enter the no:")

m1 = int(input("enter maths marks:"))
m2 = int(input("enter physics marks:"))
m3 = int(input("enter chemistry marks:"))
m4 = int(input("enter biology marks:"))
m5 = int(input("enter graphics marks:"))

total = m1 + m2 + m3 + m4 + m5
percentage = total/5

if percentage <= 90:
    grade = "B"
elif percentage >= 90:
    grade = "A"
elif percentage >=95:
    grade = "A+"
elif percentage <= 60:
    grade = "B"
elif percentage <= 50:
    grade = "C"
else:
    print("fail")

print("\n====STUDENT RESULT====")
print("Name", Name)
print("roll number:", rollno)
print("total marks:",total,"/500")
print("percentage:", percentage, "%")
print("grade:", grade)
