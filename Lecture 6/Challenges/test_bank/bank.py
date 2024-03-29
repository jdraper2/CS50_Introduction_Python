# In a file called bank.py, implement a program that prompts the user for a greeting. If the greeting starts with “hello”, output $0. If the greeting starts with an “h” (but not “hello”), output $20. Otherwise, output $100. Ignore any leading whitespace in the user’s greeting, and treat the user’s greeting case-insensitively.

# Import the regular expression module
import re

# Define the main function
def main():
    # Ask the user for a greeting
    greeting = input("Greeting: ")
    # Check the greeting and print the corresponding amount
    print(value(greeting))

# Define a function that checks a greeting and returns an amount
def value(greeting):
    # Convert the response to lowercase and remove leading and trailing whitespace
    greeting = greeting.lower().strip()

    # If the response starts with "hello", return "$0"
    if re.match(r'^hello', greeting):
        return "$0"
    # If the response starts with "h" (but not "hello"), return "$20"
    elif re.match(r'^h', greeting):
        return "$20"
    # If the response starts with anything else, return "$100"
    else:
        return "$100"

# Call the main function
if __name__ == "__main__":
    main()