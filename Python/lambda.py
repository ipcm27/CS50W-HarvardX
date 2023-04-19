people = [
    {"name":"Harry Potter", "house":"Gryfindor"},
    {"name":"Malfoy", "house":"Slytherin"},
    {"name":"Cho", "house":"RavenClaw"},
    {"name": "Morena", "house": "Abacate"}
]

def mamute(person):
    return person['house']

# people.sort(key=mamute)
people.sort(key = lambda person: person["name"])

print(people)
