
print("===== SIMPLE BILLING SYSTEM =====")

items = []
total = 0

n = int(input("Enter number of products: "))

for i in range(n):
    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    amount = quantity * price
    total += amount

    items.append([name, quantity, price, amount])

print("\n========== CUSTOMER BILL ==========")
print("Product\tQty\tPrice\tAmount")

for item in items:
    print(item[0], "\t", item[1], "\t",
          item[2], "\t", item[3])

print("-----------------------------------")
print("Total Amount: Rs.", total)
print("===================================")
print("Thank you! Visit Again!")
