# Define the main function
def main():
    # Ask the user for a sentence
    sentence = input(">")
    # Convert emoticons in the sentence to emojis
    sentence = convert(sentence)
    # Print the converted sentence
    print(sentence)

# Define a function that converts emoticons to emojis
def convert(sentence):
    # Replace happy emoticons with happy emojis
    sentence = sentence.replace(":)", "🙂")
    # Replace sad emoticons with sad emojis
    sentence = sentence.replace(":(", "🙁")
    # Return the converted sentence
    return sentence

# Call the main function
main()