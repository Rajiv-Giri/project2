menu={
    'pizz':40,
    'pasta':50,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}

print("Welcome to python Restaurant")
print("pizza: Rs40\npasta: Rs50\nBurger: rs60\nSalad: Rs70\nCoffee: Rs80")

order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in menu:
    order_total += menu[item_1]
    print("your item {item_1} has been added to your order")

else:
    print("ordered item {item_1} is not avaialable yet")

another_order = input("Do you want to add another item? (yes/No)")
if another_order == "yes":
    item_2 = input("Enter the name of second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print("your item {item_2} has been added to your order")
    else:
        print("Ordered item {item_2} is not avaialable!")

print("The total amount of items to pay is {order_total}")
