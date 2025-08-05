alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print()

alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)
alien_1['color'] = 'red'
print(alien_1)

print()

alien_0['speed'] = 'medium'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0["speed"] == "medium":
    x_increment = 2
else:
    x_increment = 3
alien_0["x_position"] = alien_0["x_position"] + x_increment
print(alien_0)

print()

#Removing Key-Value Parirs
print(alien_1)
del alien_1["points"]
print(alien_1)

print()

#Uing get() to access values
point_value = alien_1.get('points', 'No point assigned.')
print(point_value)
print(alien_1.get('color', 'No color assigned.'))

print()

# Looping through a dictionary

favourite_languages = {
        "jen": "python",
        "sarah": "c",
        "edward": 'rust',
        "phil": "python"
        }
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")
