# Define the main function
def main():
    # Ask the user for the value of x and convert it to an integer
    x = int(input("What is x: "))
    # Print the square of x
    print("x squared is:", square(x))

# Define a function that squares a number
def square(n):
    # Return the square of n
    return pow(n, 2)

# Call the main function
main()