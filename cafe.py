menu = {
    'Pizza':90,
    'Burger':50,
    'Pasta':70,
    'Salad':60,
    'coffee':80,
}

print("Welcome to Our Restaurant")
print("Pizza: Rs90\nBurger: Rs50\nPasta: Rs70\nSalad: Rs60\nCoffee: Rs80")

order_total = 0
item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else:
    print(f"Ordered item {item_1} is not available")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_2 = input("Enter the name of second item = ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"item {item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not available")

another_order = input("Do you want to add another item? (Yes/No)")
if another_order == "Yes":
    item_3 = input("Enter the name of third item = ")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"item {item_3} has been added to order")
    else:
        print(f"Ordered item {item_3} is not available")

print(f"The total amount of item is {order_total}")