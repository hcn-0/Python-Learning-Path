def favorite_book(title):
    print(f"One of my favorite book is {title}")

favorite_book("Alice in Wonderland")

def describe_pet(animal_type, pet_name):
    print(f"I have a {animal_type}")
    print(f"And its name is {pet_name}")

describe_pet(pet_name = "harry", animal_type = "Hamster")
 

def shirt(size = "L", message = "I hate Python"):
    print(f"Size {size}\nMessage {message}.")
shirt("M")

print()
print()

def make_album(artist_name, title, number_of_songs = None):
    album = {"artist_name": artist_name, "title": title}
    if number_of_songs:
        album["number of songs"] = number_of_songs
    return album

print(make_album("osamu", "bot kak tak"))
print(make_album("book", "bink sake", 1))


print()
print()

def print_models(unprinted_designs, completed_models):
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        completed_models.append(current_design)
def show_completed_models(completed_models):
    for c in completed_models:
        print(c)

unprinted_designs = ['phone case', 'robot', 'nothing']
completed_models = []
print(unprinted_designs)

print_models(unprinted_designs[:], completed_models)
show_completed_models(completed_models)
print(unprinted_designs)
