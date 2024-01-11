# Define the main function
def main():
    # Call the get_number function and store its return value in the variable 'number'
    number = get_number()
    # Call the meow function with 'number' as an argument
    meow(number)

# Define the get_number function
def get_number():
    # Start an infinite loop
    while True:
        # Prompt the user for input and convert it to an integer
        n = int(input("What's n: "))
        # If the input is greater than 0, return the input and end the function
        if n > 0:
            return n

# Define the meow function with one parameter 'n'
def meow(n):
    # For loop will iterate 'n' times
    for _ in range(n):
        # Print "meow" to the console
        print("meow")

# If this script is run directly, call the main function
if __name__ == "__main__":
    main()