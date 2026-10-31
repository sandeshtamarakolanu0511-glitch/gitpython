
subjects = ["Maths", "Science", "English"]

scores = []

for subject in subjects:
    print("\n", subject)
    exam1 = int(input("Enter first exam marks: "))
    exam2 = int(input("Enter second exam marks: "))
    scores.append((subject, exam1, exam2))

total = 0

print("\n--- Performance Report ---")

for subject, exam1, exam2 in scores:
    change = exam2 - exam1
    total += exam2

    print(subject, "Change:", change)

    if exam2 < 40:
        print("Weak Subject")

average = total / len(subjects)

print("Average Marks:", average)

if average >= 75:
    print("Excellent Performance")
elif average >= 50:
    print("Average Performance")
else:
    print("Poor Performance")
