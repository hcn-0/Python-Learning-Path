#students = ["Hermione", "Harry", "Ron", "Draco"]

"""for std in students:
    print(std)

for i in range(len(students)):
    print(students[i])
"""

students = {
        "Hermione": "Gryffindor",
        "Harry": "Gryffindor",
        "Ron": "Gryffindor",
        "Draco": "Slytherin",
        }


for student in students:
    print(student, students[student], sep = ": ")


students1 = [
        {"Name": "Hermione", "House": "Gryffiondor", "Patronus": "Otter"},
        {"Name": "Harry", "House": "Gryffindor", "Patronus": "Stag"},
        {"Name": "Ron", "House": "Gryffindor", "Patronus": "Jack Rusell terrir"},
        {"Name": "Draco", "House": "Slytherin", "Patronus": None}
        ]

print()
for std in students1:
   # print(f"{std["Name"]}: {std["House"]}")
   print(std["Name"], std["House"], std["Patronus"], sep = ", ")




