# This program allows a user to place an order from a menu

# The main function
def main():
    # Initialize the total price to 0.00
    total_price = 0.00

    # Start an infinite loop
    while True:
        try:
            # Prompt the user for a menu item
            menu_item = input("Item: ")
            # Convert the user's input to title case
            menu_item = menu_item.title()
            # Add the price of the menu item to the total price
            total_price += float(check_price(menu_item))
            # Print the total price, formatted to two decimal places
            print(f"Total: ${total_price:.2f}")
        # If the user inputs EOF (End of File, typically Ctrl-D)
        except EOFError:
            # Exit the program
            quit()
        # If a ValueError occurs (e.g., the input can't be converted to a float)
        except ValueError:
            # Ignore the error and continue with the next iteration of the loop
            pass

# Function to check the price of a food item
def check_price(food):
    # Define a dictionary with the menu items and their prices
    menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }

    # If the food item is in the menu
    if food in menu:
        # Return the price of the food item
        return menu[food]
    # If the food item is not in the menu
    else:
        # Return 0.00
        return 0.00

# Call the main function
main()