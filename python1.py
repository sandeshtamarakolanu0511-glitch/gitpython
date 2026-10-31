
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)

    name = input("Enter student name: ")

    marks = []
    for j in range(3):
        mark = float(input("Enter subject mark: "))
        marks.append(mark)

    attendance = float(input("Enter attendance percentage: "))
    income = float(input("Enter fa"))
                         
    total = sum(marks)
    aggregate = total / 3

    # Check scholarship eligibility
    if (aggregate >= 75 and min(marks) >= 50
        and attendance >= 80 and income <= 250000):

        students.append((name, aggregate, attendance))

# Sort by aggregate marks, then attendance
students.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\n--- Scholarship Eligible Students ---")

if len(students) == 0:
    print("No students are eligible.")
else:
    rank = 1

    for student in students:
        name, aggregate, attendance = student

        print("Rank:", rank)
        print("Name:", name)
        print("Aggregate:", round(aggregate, 2))
        print("Attendance:", attendance)
        print()
        rank = rank + 1
