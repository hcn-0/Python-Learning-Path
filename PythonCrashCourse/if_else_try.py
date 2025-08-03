#5.3
alien_color = 'green'

if alien_color == 'green':
    print("Your eran 5 point")
else:
    print("You fail!, tr again")

#5.4
if alien_color == 'green':
    print("You earn 5 points")
elif alien_color != 'green':
    print("You earn 10 points")
#5.5
if alien_color == 'green':
    print("5 points")
elif alien_color == 'yellow':
    print("10 points")
elif alien_color == 'red':
    print("15 points")
else:
    print("Try again")

#5.L
favorite_frutis = ['apple', 'orange', 'lemon']
if 'apple' in favorite_frutis:
    print("You really like apples")


#5.8
user_names = ['osamu', 'luffy', 'zoro', 'admin', 'nami']

for user in user_names:
    if user == 'admin':
        print(f"Hello {user}, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in again.")

#5.10

