# Implement a program that prompts consumers users to input a fruit (case-insensitively) 
# and then outputs the number of calories in one portion of that fruit, per the FDA’s 
# poster for fruits. Ignore any input that isn’t a fruit.

# Define the main function
def main():
    # Prompt the user for a fruit
    fruit = input("Item: ")
    # Call the check_fruit function with the lowercase version of 'fruit' as an argument
    check_fruit(fruit.lower())

# Define the check_fruit function with one parameter 'f'
def check_fruit(f):
    # Define a dictionary 'fruits' where each key is a fruit and each value is the number of calories in one portion of that fruit
    fruits = {
        "apple": "130",
        "avacado": "50",
        "banana": "110",
        "cantaloupe": "50",
        "grapefruit": "60",
        "grapes": "90",
        "honeydew": "50",
        "sweet cherries": "100"
    }

    # If 'f' is a key in 'fruits'
    if f in fruits:
        # Print "Calories: " followed by the value associated with the key 'f' in 'fruits'
        print("Calories: " + fruits[f])
    # If 'f' is not a key in 'fruits'
    else:
        # Do nothing
        pass

# Call the main function
main()