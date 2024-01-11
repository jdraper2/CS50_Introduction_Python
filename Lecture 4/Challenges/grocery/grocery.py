# This program prompts the user for grocery items until the user inputs EOF (typically Ctrl-D)
# It then outputs the user's grocery list in uppercase, sorted alphabetically by item
# Each line is prefixed with the number of times the user inputted that item

# Define the main function
def main():
    # Initialize an empty dictionary to store the shopping items
    shopping_items = {}

    # Start an infinite loop
    while True:
        try:
            # Prompt the user for a grocery item
            item = input("")
            # If the item is already in the dictionary
            if item in shopping_items.keys():
                # Increment the count of the item by 1
                amount = int(shopping_items[item]) + 1
                # Update the count of the item in the dictionary
                shopping_items.update({item:amount})
            # If the item is not in the dictionary
            else:
                # Add the item to the dictionary with a count of 1
                shopping_items.update({item:1})
        # If the user inputs EOF (End of File, typically Ctrl-D)
        except EOFError:
            # Break the loop
            break

    sorted_shopping_items = sorted(shopping_items.items(), key=lambda x:x[0])
    # For each item in the dictionary
    for sorted_shopping_item in sorted_shopping_items:
        # Print the count and the item in uppercase
        print(str(sorted_shopping_item[1]) + "  " + str(sorted_shopping_item[0]).upper())

# Call the main function
main()