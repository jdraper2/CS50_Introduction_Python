# Define the main function
def main():
    # Ask the user for the value of x and convert it to an integer
    x = int(input("What's x: "))
    # Check if x is even
    if is_even(x):
        # If x is even, print "Even"
        print("Even")
    else:
        # If x is not even (i.e., it's odd), print "Odd"
        print("Odd")

# Define a function that checks if a number is even
def is_even(n):
    # If the remainder of n divided by 2 is 0, the number is even
    return n % 2 == 0

# Call the main function
main()