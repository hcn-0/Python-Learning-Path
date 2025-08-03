
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

#checking in list
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# Using if Statements with Lists
requested_toppings = ['mushrooms', 'green papers', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping == 'green papers':
        print(f"Sorry, we are out of {requested_topping} right now.")
    else:
        print(f"Adding {requested_topping}")
print("Finished making pizza")

# Using multiple Lists
print("\n")

available_toppings = ['mushrooms', 'olives', 'green papers', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}")
    else:
        print(f"Sorry, we are out of {requested_topping} right now.")


