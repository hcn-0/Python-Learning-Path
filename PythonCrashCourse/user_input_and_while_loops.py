#ask = input("Wat is the type of rental car you like?:")
#print(f"Let me see if I can find you a {ask}")

"""n = int(input("Enter a number: "))

if n % 10 == 0:
    print("Number is multiple of 10")
else:
    print("Number is not multiple of 10")

"""
'''
while True:
    pizzas = input("Enter pizza toppings (type quit if you done): ")
    if pizzas != "quit":
        print(f"I'll add {pizzas} to pizza")
    else:
        break
'''

ucu = ["alice", "brain", "candace"]
cu = []

while ucu:
    cru = ucu.pop()
    print(f"Varifying user: {cru}")
    cu.append(cru)

print("Following users have been confiremed:")

for u in cu:
          print(u.title())
