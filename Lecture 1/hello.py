# Ask a user for their name.
name = input('What\'s your name? ').strip().title()  # User input for name.

# Remove the whitespaces from the string
# name = name.strip()

#Capitalise the users name
# name = name.capitalize()

#Chain two functions together
# name = name.strip().title()

# Print a greeting that includes the user's name.
# Here, the 'sep' parameter is used to specify the separator between the arguments.
print ("Hello,", name, sep="+")  # Display greeting with '+' as a separator.

# Print the greeting in two parts.
# The 'end' parameter is used to specify what should be printed at the end. 
# By default, it's a newline, but here it's changed to an empty string, so the next print continues on the same line.
print("Hello, ", end="")
print(name)  # This will continue on the same line as the previous print statement.

# Print a greeting using a formatted string literal (f-string).
# This allows for the inclusion of the value of variables directly in the string by enclosing them in {}.
print(f"Hello, {name}")  # Display greeting using f-string.

# Split users name into first name and last name
first, last = name.split(" ")

print(f"Hello, {first}")