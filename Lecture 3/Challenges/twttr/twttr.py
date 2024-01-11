#When texting or tweeting, it’s not uncommon to shorten words to save time or space, as by omitting vowels, much like Twitter was originally called twttr. In a file called twttr.py, implement a program that prompts the user for a str of text and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.
import re

def main():
    tweet = input("Input: ")
    print("Output: " + convert_tweet(tweet))

def convert_tweet(input):
    pattern = re.compile('[aeiouAEIOU]')
    result = re.sub(pattern, '', input)
    return result

# If this script is run directly (not imported as a module), call the main function
if __name__ == "__main__":
    main()