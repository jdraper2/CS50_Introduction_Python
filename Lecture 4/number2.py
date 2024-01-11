# Define the main function
def main():
    # Call the get_int function and assign its return value to x
    x = get_int()
    # Print the value of x
    print(f"x is {x}")

# Define a function to get an integer input from the user
def get_int():
    # Keep asking for input until a valid integer is provided
    while True:
        try:
            # Try to convert the user's input to an integer and assign it to x
            x = int(input("What's x: "))
        # If a ValueError occurs (i.e., the input can't be converted to an integer), print an error message
        except ValueError:
            print("X is not an integer")
        # If no exception was raised in the try block, break the loop
        else:
            break
    # Return the value of x
    return x

# Call the main function
main()