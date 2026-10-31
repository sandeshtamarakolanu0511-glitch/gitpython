
branches = ["Branch 1", "Branch 2", "Branch 3"]
products = ["Mobile", "Laptop", "Tablet"]

sales = []

for branch in branches:
    print("\n", branch)
    data = []

    for product in products:
        amount = int(input("Enter sales of " + product + ": "))
        data.append(amount)

    sales.append(data)

print("\n--- Sales Report ---")

for i in range(3):
    print(branches[i], "Total Sales:", sum(sales[i]))
    best = sales[i].index(max(sales[i]))
    print("Best Product:", products[best])

print("\n--- Product Total Sales ---")

for j in range(3):
    total = 0
    for i in range(3):
        total += sales[i][j]

    print(products[j], ":", total)

best_branch = sales.index(max(sales, key=sum))
print("\nBest Performing Branch:", branches[best_branch])
