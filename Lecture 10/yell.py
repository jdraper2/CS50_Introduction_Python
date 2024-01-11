# This is the main function that calls all the other functions
def main():
    yell("This is CS50")  # Calls the yell function with a string
    yell2(["This", "is", "CS50"])  # Calls the yell2 function with a list of strings
    yell3("This", "is", "CS50")  # Calls the yell3 function with multiple string arguments
    yell4("This", "is", "CS50")  # Calls the yell4 function with multiple string arguments
    yell5("This", "is", "CS50")  # Calls the yell5 function with multiple string arguments

# This function takes a string and prints it in uppercase
def yell(phrase):
    print(phrase.upper())

# This function takes a list of strings, converts each string to uppercase, and prints them
def yell2(words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

# This function takes multiple string arguments, converts each to uppercase, and prints them
def yell3(*words):
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)

# This function takes multiple string arguments, converts each to uppercase using map, and prints them
def yell4(*words):
    uppercased = map(str.upper, words)
    print(*uppercased)

# This function takes multiple string arguments, converts each to uppercase using list comprehension, and prints them
def yell5(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)

# This checks if the script is being run directly and not imported, and if so, calls the main function
if __name__ == "__main__":
    main()