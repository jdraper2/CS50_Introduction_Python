# In plates.py, implement a program that prompts the user for a vanity plate and then output Valid if meets all of the requirements or Invalid if it does not. Assume that any letters in the user’s input will be uppercase. Structure your program per the below, wherein is_valid returns True if s meets all requirements and False if it does not. Assume that s will be a str. You’re welcome to implement additional functions for is_valid to call (e.g., one function per requirement).

# Define the main function
def main():
    # Prompt the user for a vanity plate
    plate = input("Plate: ")
    # If the plate is valid, print "Valid"
    if is_valid(plate):
        print("Valid")
    # If the plate is not valid, print "Invalid"
    else:
        print("Invalid")

# Define the is_valid function with one parameter 's'
def is_valid(s):
    # Initialize a counter for the number of numeric characters
    number_count = 0

    # If the length of 's' is between 2 and 6 (inclusive)
    if len(s) >= 2 and len(s) <= 6:
        # Iterate over each character in 's'
        for i in range(len(s)):
            # If the first or second character is not a letter, return False
            if s[0].isalpha() != True or s[1].isalpha() != True :
                return False
            else:
                # If the current character is not a number or a letter, return False
                if s[i].isnumeric() != True and s[i].isalpha() != True:
                    return False
                
                # If the current character is a number
                if s[i].isnumeric() == True:   
                    # Increment the number counter
                    number_count += 1
                    # If the first number is 0, return False
                    if number_count == 1 and s[i] == "0":
                        return False
                
                # If there is more than one number and the current character is a letter, return False
                if number_count > 1 and s[i].isalpha() == True:
                    return False
        # If none of the conditions for invalidity are met, return True
        return True

# If this script is run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()