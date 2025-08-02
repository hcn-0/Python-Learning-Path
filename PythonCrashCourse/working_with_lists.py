# range() function

for value in range(1,5):
    print(value)

# make a list of numbers using range()

squres = []
for value in range(1,11):
    squre = value ** 2
    squres.append(squre)
print(squres)

#simple statistics with a list of numbers

digits = [1,2,3,4,5,6,7,8,9,10]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
"""squares = [value ** 2 for value in range(1,11)]
print(squares)"""

# Try
#4.3
for v in range(1,21):
    print(v)
#4.5
"""one_million = list(range(1,10000000))
print(min(one_million))
print(max(one_million))
print(sum(one_million))"""

#4.6
odd = [value for value in range(1,21,2)]
print(odd)

#4.7
multiple_of_three = [value*3 for value in range(3,31)]
print(multiple_of_three)

#4.9
cubes = [c**3 for c in range(1,11)]
print(cubes)
