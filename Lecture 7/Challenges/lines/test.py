with open("name.txt") as file:
    for line in sorted(file):
        print("Hello, ", line.rstip())