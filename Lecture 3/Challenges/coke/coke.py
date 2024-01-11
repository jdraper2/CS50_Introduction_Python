# Implement a program that prompts the user to insert a coin, one at a time, 
# each time informing the user of the amount due. Once the user has inputted 
# at least 50 cents, output how many cents in change the user is owed. 
# Assume that the user will only input integers, and ignore any integer 
# that isn’t an accepted denomination.

def main():
    # Initialize the amount due as 50 cents
    amount_due = 50
    # Print the initial amount due
    print("Amount Due: " + str(amount_due))

    # Start an infinite loop
    while True:
        # Prompt the user to insert a coin
        amount_deposited = input("Insert Coin: ")

        try:
            # If the amount deposited is a 5, 10, or 25 cent coin
            if amount_deposited == "5" or amount_deposited == "10" or amount_deposited == "25":
                # Subtract the amount deposited from the amount due
                amount_due -= int(amount_deposited)

            # If the amount due is exactly 0
            if int(amount_due) == 0:
                # Print that the change owed is 0
                print("Change Owed: 0")
                # Break the loop
                break
            # If the amount due is less than 0
            elif int(amount_due) < 0:
                # Calculate the change owed
                n = int(amount_due * -1)
                # Print the change owed
                print("Change Owed: " + str(n))
                # Break the loop
                break

            # Print the updated amount due
            print("Amount Due: " + str(amount_due))

        # Catch any exceptions like ValueError or ZeroDivisionError
        except (ValueError, ZeroDivisionError):
            pass

# Call the main function
main()