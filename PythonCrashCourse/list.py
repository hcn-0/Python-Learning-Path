# Modifying Elements in a List

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

motorcycle[0] = 'ducati' #change value
print(motorcycle)

# Adding Elements to a List
motorcycle.append('bmw')
print(motorcycle)

# Insert elemensts any location
motorcycle.insert(0,'lambo')
print(motorcycle)

motorcycle.insert(3, 'bugati') # add in index 3 and after all element will be right shshift
print(motorcycle)

#Removing Item 
motorcycle.pop() # remove the last item
print(motorcycle)

#poping from any possition
motorcycle.pop(3)
print(motorcycle)

#Removing by value
motorcycle.remove('lambo')
print(motorcycle)

# Try Yourself 
#3.4 Guest List
want_to_invite = ['luffy', 'zoro', 'sanji']
print(f"{want_to_invite[0].title()} you are invited for dinner")
print(f"{want_to_invite[1].title()} you are invited for dinner")
print(f"{want_to_invite[2].title()} you are invited for dinner")

print(f"{want_to_invite[1].title()} im busy")

want_to_invite[1] = 'nami' # replace with zoro

print(f"{want_to_invite[0].title()} you are invited for dinner")
print(f"{want_to_invite[1].title()} you are invited for dinner")
print(f"{want_to_invite[2].title()} you are invited for dinner")


# Sorting List with sort() method

cars = ['bmw', 'toyota', 'subaru']

cars.sort()
print(cars)

numbers = [3,6,3,1,6]
print(f"Orginal List {numbers}.")
print(f"Afert Temporaray Sorted with sorted() method.")
print(sorted(numbers))
print(f"Orginal List: {numbers}")

