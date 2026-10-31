
total = int(input("Enter total classes: "))
attended = int(input("Enter attended classes: "))
threshold = float(input("Enter required attendance percentage: "))

percentage = attended / total * 100

print("Current Attendance:", round(percentage, 2), "%")

if percentage >= threshold:
    print("You are already eligible.")
else:
    required = 0

    while (attended + required) / (total + required) * 100 < threshold:
        required += 1

    print("Minimum consecutive classes to attend:", required)
    print("Future attendance will be 100%.")

