# Import the sys module to access command line arguments and system-specific parameters
import sys

# Use a try-except block to handle potential errors
try:
    # Try to print a greeting message with the first command line argument
    # sys.argv[0] is the script name, so sys.argv[1] would be the first actual argument
    print("Hello, my name is ", sys.argv[1])

# If an IndexError occurs (i.e., there are no command line arguments)
except IndexError:
    # Print an error message
    print("Too few arguments")