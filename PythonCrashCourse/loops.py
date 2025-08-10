#while True:
   # age = int(input("Eter your age: "))
   # if age < 3:
   #     print("Ticket if free")
   # elif 3 <= age <= 12:
    #    print("Ticket is $10")
   # else:
    #    print("Ticket is $15")

unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print(f"verifying user: {current_user.title()}")
    confirmed_users.append(current_user)
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#removiing all instance of specific values from a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
while 'cat' in pets:
    pets.remove('cat')
print(pets)

print()

sandwich_orders = ['club sadwich', 'blt', 'pastrami', 'grilled cheese', 'pastrami', 'reuben', 'pastrami']

print("Deli has run out of pastrami.")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)

