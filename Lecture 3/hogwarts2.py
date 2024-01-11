# Define a dictionary of students, where each key is a student's name and each value is the student's house
students = {
    "Hermione": "Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin"
}

# (This line is commented out) Print the house of "Hermione" by accessing the value associated with the key "Hermione" in the students dictionary
# print(students["Hermione"])

# Iterate over each key (student's name) in the students dictionary
for student in students:
    # Print the student's name and the associated house, separated by a comma
    print(student, students[student], sep=", ")