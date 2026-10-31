
import math

points = []

n = int(input("Enter number of locations: "))

for i in range(n):
    x = float(input("Enter x coordinate: "))
    y = float(input("Enter y coordinate: "))
    points.append((x, y))

longest = 0
segment = 0

for i in range(n - 1):
    x1, y1 = points[i]
    x2, y2 = points[i + 1]

    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)

    print("Distance:", distance)

    if distance > longest:
        longest = distance
        segment = i + 1

print("Longest Distance:", longest)
print("Longest Segment:", segment, "to", segment + 1)
