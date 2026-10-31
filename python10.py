
students = []
ids = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    sid = input("Enter student ID: ")
    name = input("Enter name: ")
    marks = int(input("Enter marks: "))
    attendance = int(input("Enter attendance: "))
    course = input("Enter course: ")

    if sid in ids:
        print("Duplicate ID!")
        continue

    ids.append(sid)

    if name == "" or course == "":
        print("Missing details!")
    elif marks < 0 or marks > 100:
        print("Invalid marks!")
    elif attendance < 0 or attendance > 100:
        print("Invalid attendance!")
    else:
        students.append((sid, name, marks, attendance, course))
        print("Record is valid.")

print("\n--- Valid Student Records ---")

for sid, name, marks, attendance, course in students:
    print(sid, name, marks, attendance, course)

print("Total Valid Records:", len(students))
