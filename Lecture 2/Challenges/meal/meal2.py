# https://docs.python.org/3/library/stdtypes.html#string-methods

# In meal.py, implement a program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time. 
# If it’s not time for a meal, don’t output anything at all. Assume that the user’s input will be formatted in 24-hour time as #:## or ##:##. 
# And assume that each meal’s time range is inclusive. For instance, whether it’s 7:00, 7:01, 7:59, or 8:00, or anytime in between, it’s time for breakfast.


import re

# Define the main function
def main():
    # Ask the user for the current time
    current_time = input("What time is it: ")
    # Convert the time to a list of strings [hours, minutes]
    time_string = convert(current_time)
    # Check if it's breakfast time (7:00 to 8:00 AM)
    if re.match(r'.*a.m.', time_string[1]) and ((time_string[0] == "7") or (time_string[0] == "8" and re.match(r'^00', time_string[1]))):
        print("Breakfast time")
    # Check if it's lunch time (12:00 to 1:00 PM)
    elif re.match(r'.*p.m.', time_string[1]) and ((time_string[0] == "12") or (time_string[0] == "1" and re.match(r'^00', time_string[1]))):
        print("Lunch time")
    # Check if it's dinner time (6:00 to 7:00 PM)
    elif re.match(r'.*p.m.', time_string[1]) and ((time_string[0] == "6") or (time_string[0] == "7" and re.match(r'^00', time_string[1]))):
        print("Dinner time")

# Define a function that converts a time string to a list of strings [hours, minutes]
def convert(time):
    return time.split(":")

# If this script is run directly, call the main function
if __name__ == "__main__":
    main()