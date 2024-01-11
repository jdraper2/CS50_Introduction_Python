# Ask the user for their name
name = input("What's your name: ")

# Use a match-case structure to check the user's name
match name:
    # If the name is Harry, Hermione, or Ron, print "Griffindor"
    case "Harry" | "Herminone" | "Ron":
        print("Griffindor")
    # If the name is Draco, print "Slytherin"
    case "Draco":
        print("Slytherin")
    # If the name is anything else, print "Who?"
    case _:
        print("Who?")