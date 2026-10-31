
products = []
total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    name = input("\nEnter product name: ")
    category = input("Enter category (food/electronics): ")
    price = float(input("Enter price: "))
    qty = int(input("Enter quantity: "))

    tax = 5 if category == "food" else 18

    amount = price * qty
    gst = amount * tax / 100
    total = total + amount + gst

    products.append((name, qty, amount, gst))

# Discount rules
discount = 0

if total >= 5000:
    discount = total * 0.20
elif total >= 2000:
    discount = total * 0.10

# Maximum discount limit
if discount > 1000:
    discount = 1000

print("\n----- INVOICE -----")

for name, qty, amount, gst in products:
    print(name, "Qty:", qty, "Price:", amount, "Tax:", gst)

print("Total:", round(total, 2))
print("Discount:", round(discount, 2))
print("Final Bill:", round(total - discount, 2))
