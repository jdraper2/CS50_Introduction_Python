import random
#from random import choice

coin = random.choice(["heads", "tails"])
print(coin)

number = random.randint(1, 10)
print(number)

cards = ["Jack", "Queen", "King"]
random.shuffle(cards)

for card in cards:
    print(card)