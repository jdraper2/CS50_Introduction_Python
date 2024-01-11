students = ["Hermione", "harry", "Ron"]

gryffindors = []

for student in students:
    gryffindors.append({"name": student, "house": "Gryffindor" })

print(gryffindors)


gryffindors2 = [{"name": student, "house": "Gryffindor"} for student in students]

print(gryffindors2)

gryffindors3 = {student: "Gryffindor" for student in students}

print(gryffindors3)