# Start an infinite loop
while True:
    try:
        # Try to convert the user's input to an integer and assign it to x
        x = int(input("What's x: "))
    # If a ValueError occurs (i.e., the input can't be converted to an integer)
    except ValueError:
        # Print an error message
        print("X is not an integer")
    # If no exception was raised in the try block
    else:
        # Break the loop
        break

# Print the value of x
print(f"x is {x}")