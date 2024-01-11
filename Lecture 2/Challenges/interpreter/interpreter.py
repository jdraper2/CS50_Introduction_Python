# In a file called interpreter.py, implement a program that prompts the user for an arithmetic expression and then calculates and outputs the result as a floating-point value formatted to one decimal place. Assume that the user’s input will be formatted as x y z, with one space between x and y and one space between y and z, wherein:

# Define the main function
def main():
    # Prompt the user for an arithmetic expression
    expression = input("Expression: ")
    # Calculate the result of the expression and print it
    print(calculate_expression(expression))

# Define a function that calculates the result of an arithmetic expression
def calculate_expression(exp):
    # Split the expression into a list of strings
    exp = exp.split()

    # Use a match-case structure to check the operator in the expression
    match exp[1]:
        # If the operator is "+", add the two numbers
        case "+":
            return float(exp[0]) + float(exp[2])
        # If the operator is "-", subtract the second number from the first
        case "-":
            return float(exp[0]) - float(exp[2])
        # If the operator is "*", multiply the two numbers
        case "*":
            return float(exp[0]) * float(exp[2])
        # If the operator is "/", divide the first number by the second
        case "/":
            return float(exp[0]) / float(exp[2])
        # If the operator is anything else, return an error message
        case _:
            return "Unknown expression."

# Call the main function
main()