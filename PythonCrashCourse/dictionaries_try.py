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
