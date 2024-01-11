# Define the main function
def main():
    # Call the print_square function with 3 as an argument
    print_square(3)

# Define the print_square function with one parameter 'size'
def print_square(size):
    # For loop will iterate 'size' times
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

# Call the main function
main()