# Implement a program that prompts the user for a fraction, formatted as X/Y, 
# wherein each of X and Y is an integer, and then outputs, as a percentage rounded 
# to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, 
# output E instead to indicate that the tank is essentially empty. And if 99% or more 
# remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt 
# the user again. (It is not necessary for Y to be 4.) Be sure to catch any exceptions 
# like ValueError or ZeroDivisionError.

def main():
    # Start an infinite loop
    while True:
        # Prompt the user for input
        fraction = input("Fraction: ")
        # Call the check_reading function with 'fraction' as an argument
        reading_values = check_reading(fraction)
        # If the return value of check_reading is not False, break the loop
        if reading_values != False:
            break

    # If 'reading_values' is not a float, print 'reading_values'
    if isinstance(reading_values, float) == False:
        print(reading_values)
    # Otherwise, print 'reading_values' as a percentage rounded to the nearest integer
    else:
        print(f"{float(reading_values):.0%}")

def check_reading(reading):
    # Split 'reading' into a list of strings at each "/"
    reading = reading.split("/")

    try:
        # If the first value in 'reading' is greater than the second value, return False
        if int(reading[0]) > int(reading[1]):
            return False

        # Calculate the fraction as a float
        reading = int(reading[0]) / int(reading[1])

        # If 'reading' is 99% or more, return "F"
        if float(reading) >= 0.99:
            return "F"
        # If 'reading' is 1% or less, return "E"
        elif float(reading) <= 0.01:
            return "E"
        # Otherwise, return 'reading'
        else:
            return reading
    # Catch any exceptions like ValueError or ZeroDivisionError
    except (ValueError, ZeroDivisionError):
        return False

# Call the main function
main()