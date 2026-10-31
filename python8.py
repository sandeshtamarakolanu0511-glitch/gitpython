
students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    students.append((name, score))

students.sort(key=lambda x: x[1], reverse=True)

g = int(input("Enter number of groups: "))

groups = [[] for i in range(g)]
totals = [0] * g

for student in students:
    index = totals.index(min(totals))
    groups[index].append(student)
    totals[index] += student[1]

for i in range(g):
    print("\nGroup", i + 1)
    for name, score in groups[i]:
        print(name, score)
    print("Total Score:", totals[i])
