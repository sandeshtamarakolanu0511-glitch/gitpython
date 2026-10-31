
teams = []
n = int(input("Enter number of teams: "))

for i in range(n):
    name = input("\nEnter team name: ")
    wins = int(input("Enter wins: "))
    draws = int(input("Enter draws: "))
    losses = int(input("Enter losses: "))
    goals = int(input("Enter goal difference: "))

    points = wins * 3 + draws
    teams.append((name, points, goals))

# Sort by points and goal difference
teams.sort(key=lambda x: (x[1], x[2]), reverse=True)

print("\n--- Tournament Rankings ---")

rank = 1
for name, points, goals in teams:
    print(rank, name, "Points:", points, "Goal Difference:", goals)
    rank += 1
