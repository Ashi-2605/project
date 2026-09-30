menu={
    'Pizza':60,
    'Sandwitch':50,
    'Dahi panipuri':30,
    'Burger':70,
    'Momos':60,
}
print(menu)

#greet
print("Welcome to ASHI DELICIOUS CAFE")
print("Pizza :60\n Sandwitch:50\n Dahi panipuri:30\n Burger:70\n Momos:60\n")

order_total=0

item_1=input("Enter the name of item you want to order=")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your Item {item_1} has been added to your order")

else:
    print("Ordered item {item_1} is not avaialable yet!")

another_order=input("Do you want to add another item ?(Yes/No)")
if another_order=="Yes":
    item_2=input("Enter  the name of your second item=")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Item{item_2} has been added to order")
    else:
        print(f"Ordered item {item_2} is not avaialable!")


print(f"The total amount of items to pay  is {order_total}")
    


