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



alien_2 = {"color": "blue", "points": 15}
aliens = [alien_0, alien_1, alien_2]
print()
for alien in aliens:
    print(alien)

print()

g_aliens = []

#make 30 green aliens.
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5, "speed": "slow"}
    g_aliens.append(new_alien)
for alien in g_aliens[:5]:
    print(alien)

print()
#change alien
for alien in g_aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["points"] = 10
        alien["speed"] = "medium"


for alien in g_aliens[:5]:
    print(alien)

print()

# A List in a Dictionary

pizza = {
        "crust": "thik",
        "toppings": ["mushrooms", "extra cheese"],
        }
print(f"You ordered a {pizza["crust"]}-crust pizza with the following toppings:")
for topping in pizza["toppings"]:
    print(topping)

print()

favourite_languages = {
        "jen": ["python", "rust"],
        "sarah": ["c"],
        "edward": ["rust", "go"],
        "phil": ["python", "haskell"],
        }
for name, languages in favourite_languages.items():
    print(f"{name.title()}'s favourite languages are:", end = " ")
    for language in languages:
        print(language, end = " ")
    print()

print()

# A Dictionary in a Dictionary
users = {
        "aeinstein": {
            'first': 'albert',
            'last': 'einstein',
            'location': 'princenton',
            },
        "mcurie": {
            'first': 'marie',
            'last': 'curie',
            'location': 'paris',
            },
        }
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    for k,v in user_info.items():
        print(k,v , sep = ': ')


