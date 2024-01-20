# DECLARING A DICTIONARY

# new_dict = {}

# new_dict = dict() # new dictionary

# user = {
#     'username': 'Dylank',
#     # key(unlocks value): value
#     'password': '123', # or 123
#     'fav_color': 'green',
# }

# print(type(new_dict))

# print(user)


# ACCESSING VALUES

# use the key corresponding to the value

# user = {
#     'username': 'Dylank',
#     # key(unlocks value): value
#     'password': '123', # or 123
#     'fav_color': 'green',
# }

# print(user['username'])


# ADDING NEW PAIRS

# user = {
#     'username': 'Dylank',
#     # key(unlocks value): value
#     'password': '123', # or 123
#     'fav_color': 'green',
# }

# # create new key you want
# user['fav_food'] = 'Tacos'
# print(user)

# user['pet'] = 'dog'
# print(user)


#MODIFYING VALUES
#change value of a particular key

# user = {
#     'username': 'Dylank',
#     # key(unlocks value): value
#     'password': '123', # or 123
#     'fav_color': 'green',
# }

# user['username'] = 'Hurricane'
# print(user)

#REMOVING KEY,VALUE PAIRS

# user = {
#     'username': 'Dylank',
#     # key(unlocks value): value
#     'password': '123', # or 123
#     'fav_color': 'green',
# }

# del user['fav_color']
# print(user)

#LOOPING A DICTIONARY

# user = {
#     'username': 'Dylank',
#     # key(unlocks value): value
#     'password': '123', # or 123
#     'fav_color': 'green',
# }

# # Create statements with F Key
# for key, value in user.items():
#     print(f"My {key} is {value}")


def shopcart():
    cart = {
        'food' : 'quant'
    }

    while True:
        food = input("Do you want to add, remove, or show a food item? If done, type 'quit' ")
        quant = input("How many? If done, type 'quit'")

        if food.lower() == 'add':
            print(input("What kind?"))

        if food.lower() == 'show':
             print(f"{food} {quant}")

        if food.lower() == 'remove':
            del [food]; quant

        if food.lower() == 'quit':
            break

        if quant.lower() == 'quit':
            break

        cart[food] = quant 
    print(cart)
    
    for food, quant in cart.items():
        if 'quit':
            print(f"{food} {quant}")

shopcart()