# Define the main function
def main():
    # Call the hello function without arguments
    hello()
    # Ask the user for their name
    name = input("What's your name? ")
    # Call the hello function with the user's name as an argument
    hello(name)

# Define the hello function with an optional argument
def hello(to="World"):
    # Print a greeting to the specified recipient
    print("Hello,", to)

# Call the main function
main()