from validator_collection import validators, checkers, errors

def main():

    print(check_email(input("What's your email address? ")))


def check_email(e):

    try:
        if validators.email(e):
            return "Valid"
    except:
        return "Invalid"


if __name__ == "__main__":
    main()
