people = [
    {"name": "Oz", "house": "Nirit"},
    {"name": "Aya", "house": "Hod HaSharon"}
]

people.sort(key=lambda person: person["name"])

print(people)