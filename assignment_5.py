# Exercise 2: Shopping Cart

prices = {"apple":0.5, "bread":2.25, "milk":3.99, "eggs":4.5}

# 1
cart = []

# 2
item1 = input("Enter name of item 1: ")
item2 = input("Enter name of item 2: ")
item3 = input("Enter name of item 3: ")

# 3
if item1 in prices:
    cart.append(item1)
else:
    print("Not sold here")

if item2 in prices:
    cart.append(item2)
else:
    print("Not sold here")

if item3 in prices:
    cart.append(item3)
else:
    print("Not sold here")

# 4
print(cart)

# 5
total = 0
if item1 in prices:
    total += prices[item1]

if item2 in prices:
    total += prices[item2]

if item3 in prices:
    total += prices[item3]

print("Total price: $" + str(round(total, 2)))

# 6
if total > 10:
    total *= 0.9
    print("10% off price: $" +str(round(total, 2)))

# BONUS
print("Number of apples: " + str(cart.count("apple")))
print(cart) # Used to find item for user to remove
item_remove = input("Enter the item you want to remove from your cart: ") # Used to determine what the user wants to remove

# The following lines are used to check if the item chosen to be removed by the user exists in the cart.
# This is done primarily to account for typos and secondarily for items that don't exist.
if item_remove in cart:
    cart.remove(item_remove)
    print(cart)
else:
    print("The item is either not in the cart or there is a typo in your input")