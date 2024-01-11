# Define the main function
def main():
    # Ask the user for the cost of the meal and convert it to a float
    dollars = dollars_to_float(input("How much was the meal? "))
    # Ask the user for the tip percentage they want to leave and convert it to a float
    percent = percent_to_float(input("What percentage would you like to tip? "))
    # Calculate the tip amount
    tip = dollars * percent
    # Print the tip amount, formatted to 2 decimal places
    print(f"Leave ${tip:.2f}")

# Define a function that converts a dollar amount to a float
def dollars_to_float(d):
    # TODO
    # Convert the dollar amount to a float and return it
    return float(d)

# Define a function that converts a percentage to a float
def percent_to_float(p):
    # TODO
    # Convert the percentage to a float and divide by 100 to get the decimal equivalent, then return it
    return float(p) / 100

# Call the main function
main()
