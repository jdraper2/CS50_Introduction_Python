# Import the sys module to access command line arguments and system-specific parameters
import sys

# Check if the number of command line arguments is less than 2
# sys.argv[0] is the script name, so sys.argv[1] would be the first actual argument
if len(sys.argv) < 2:
    # If there are too few arguments, exit the program and print an error message
    sys.exit("Too few arguments")

# Loop over each argument in the command line arguments, skipping the script name
for arg in sys.argv[1:]:
    # Print a greeting message with the argument
    print("Hello, my name is ", arg)