names = []

for _ in range(3):
    names.append(input("What's your name: "))

with open("name.txt", "a") as file:
    for name in sorted(names):
        file.write(f"{name}\n")\

with open("name.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())