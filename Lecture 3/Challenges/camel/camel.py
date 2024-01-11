# Import the regular expression module
import re

# Define the main function
def main():
    # Prompt the user for a variable name in CamelCase
    file_name = input("CamelCase: ")
    # Print "snake_case: " without a newline at the end
    print("snake_case: ", end="")
    # Call the convert_case function with 'file_name' as an argument and print the result
    print(convert_case(file_name))

# Define the convert_case function with one parameter 'name'
def convert_case(name):
    # Initialize an empty string 'sname'
    sname = ""

    # Iterate over each character 'c' in 'name'
    for c in name:
        # If 'c' is an uppercase letter
        if c.isupper() == True:
            # Add an underscore to 'sname'
            sname = sname + "_"
            # Add the lowercase version of 'c' to 'sname'
            sname = sname + c.lower()
        # If 'c' is not an uppercase letter
        else:
            # Add 'c' to 'sname'
            sname = sname + c

    # Return 'sname'
    return sname

# If this script is run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()