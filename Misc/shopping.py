shopping_list = []

num_items = int(input("How many items do you want to add? "))

for i in range(num_items):
    print("Item "+str(i+1)+":")
    item = input("Enter the item name: ")
    shop = input("Enter the shop you will visit: ")
    priority = input("Enter the priority (High/Medium/Low): ")
    bought = input("Have you bought it? (yes/no): ").lower()
    price = float(input("How much are you willing to pay (£): "))
    quantity = int(input("Enter the quantity needed: "))

    shopping_list.append({
        "item": item,
        "shop": shop,
        "priority": priority,
        "bought": bought,
        "price": price,
        "quantity": quantity
    })

print("FULL SHOPPING LIST:")
for entry in shopping_list:
    print(entry)

total = 0
for entry in shopping_list:
    if entry["bought"] == "no":
        total +=( entry["price"] * entry["quantity"])

print("Approximate total cost for your shopping trip: £"+str(total))
