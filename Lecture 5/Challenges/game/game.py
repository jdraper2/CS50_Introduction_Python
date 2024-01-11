#In a file called game.py, implement a program that:

#Prompts the user for a level,
    # If the user does not input a positive integer, the program should prompt again.
    # Randomly generates an integer between 1 and 
    # , inclusive, using the random module.

    # Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
        # If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
        # If the guess is larger than that integer, the program should output Too large! and prompt the user again.
        # If the guess is the same as that integer, the program should output Just right! and exit.

import random

def main():

    

    while True:
        try:
            guess = input("Level: ")
            if int(guess) > 0:
                number = random.randint(1, int(guess))
                break
        except ValueError:
            pass
        except EOFError:
            break

    guess_game(number)


def guess_game(n):

    while True:
        try:
            user_guess = input("Guess: ")
            if int(user_guess) < 0:
                pass
            elif int(user_guess) > int(n):
                print("Too large! ")
            elif int(user_guess) < int(n):
                print("Too small! ")
            elif int(user_guess) == int(n):
                print("Just right!")
                return True
        except ValueError:
            pass
        except EOFError:
            return True

if __name__ == "__main__":
    main()