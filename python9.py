
products = []
n = int(input("Enter number of products: "))

for i in range(n):
    name = input("\nEnter product name: ")
    prices = []

    for j in range(3):
        price = float(input("Enter price: "))
        prices.append(price)

    change = abs(prices[-1] - prices[0]) / prices[0] * 100
    products.append((name, change))

threshold = float(input("\nEnter fluctuation threshold: "))

maximum = 0

print("\n--- Price Report ---")

for name, change in products:
    print(name, "Change:", round(change, 2), "%")

    if change > maximum:
        maximum = change

    if change > threshold:
        print("High Fluctuation!")

print("Maximum Fluctuation:", round(maximum, 2), "%")
