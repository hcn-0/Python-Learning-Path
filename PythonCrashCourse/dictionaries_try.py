info = {"first_name": "ash",
        "last_name": "katchum",
        "age": "10",
        "city": "pallet town"
        }
for k,v in info.items():
    print(k,v,sep = ': ')

print()

favourite_languages = {
        "jen": "python",
        "sarah": "c",
        "edward": 'rust',
        "phil": "python"
        }
for name, language in favourite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")


people = [
        {
            "name": "luffy",
            "age": 19,
            "city": "foosha village",
        },
        {
            "name": "ash",
            "age": 10,
            "city": "palet town",
        },
        {
            "name": "zoro",
            "age": 21,
            "city": "shimotsuki village",
        }
        ]
for person in people:
    print(f"Info of the the people i know {person}")
print()

f_numbers = {
        "luffy": [5,6],
        "zoro": [4,7,7],
        "nami": [3,9,6],
        }

for k,v in f_numbers.items():
    print(f"{k.title()}'s favourite numbers are: ",end ="")
    for n in v:
        print(n, end = " ")
    print()

