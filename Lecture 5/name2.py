# Import the sys module to access command line arguments and system-specific parameters
import sys

# Check if the number of command line arguments is less than 2
# sys.argv[0] is the script name, so sys.argv[1] would be the first actual argument
if len(sys.argv) < 2:
    # If there are too few arguments, exit the program and print an error message
    sys.exit("Too few arguments")
# Check if the number of command line arguments is more than 2
elif len(sys.argv) > 2:
    # If there are too many arguments, exit the program and print an error message
    sys.exit("Too many arguments")

# Print a greeting message with the first command line argument
print("hello, my name is ", sys.argv[1])