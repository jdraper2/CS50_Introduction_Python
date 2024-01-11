import random


def main():
    level = get_level()
    #x, y = generate_integer(level)

    score = run_game(level)
    print("Score: ", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
        except:
            pass
    return level


def generate_integer(level):

    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif level == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

def single_question(x, y):

    trys = 1

    while trys <= 3:

        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                break
            else:
                trys += 1
                print("EEE")
        except:
            trys += 1
            print("EEE")

    if trys == 1:
        return True
    if trys > 3:
        print(f"{x} + {y} = {x+y}")
        return False


    return False

def run_game(level):

    questions = 1
    score = 0

    while questions <= 10:

        try:
            x,y = generate_integer(level)

            if single_question(x, y) == True:
                score += 1

            questions += 1

        except:
            pass

    return score


if __name__ == "__main__":
    main()
