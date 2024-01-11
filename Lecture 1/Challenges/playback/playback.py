# Define the main function
def main():
    # Ask the user for a sentence
    sentence = input(">")
    # Replace all spaces in the sentence with ellipses
    sentence = sentence.replace(" ", "...")
    # Print the modified sentence
    print(sentence)

# Call the main function
main()