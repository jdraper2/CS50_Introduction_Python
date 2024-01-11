# Define a list of students, each represented as a dictionary with keys 'name', 'house', and 'patronus'
students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Sytherin", "patronus": None},
]

# Iterate over each student in the students list
for student in students:
    # Print the name, house, and patronus of the student, separated by commas
    print(student["name"], student["house"], student["patronus"], sep=", ")