import random

class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Huffelpuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))

def main():
    hat = Hat()
    hat.sort("Harry")

if __name__ == "__main__":
    main()