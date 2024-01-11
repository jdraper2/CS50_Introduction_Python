# Define the main function
def main():
    # Call the get_int function and assign its return value to x
    x = get_int("What's x: ")
    # Print the value of x
    print(f"x is {x}")

# Define a function to get an integer input from the user
def get_int(prompt):
    # Keep asking for input until a valid integer is provided
    while True:
        try:
            # Try to convert the user's input to an integer and return it
            return int(input(prompt))
        # If a ValueError occurs (i.e., the input can't be converted to an integer), just pass and ask again
        except ValueError:
            pass

# Call the main function
main()