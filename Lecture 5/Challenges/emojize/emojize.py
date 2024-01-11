# In a file called emojize.py, implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.

import emoji
import re

def main():
    user_input = input("Input: ")
    #emoji_input = re.search(':(.*):', user_input)
    #print(emoji_input.group())
    try:
        #if isinstance(emoji_input.group(), str):
            #if emoji_input.startswith(":") and emoji_input.endswith(":"):
        print(emoji.emojize(f'Output: {user_input}', language='alias'))
    except ValueError:
        pass

if __name__ == "__main__":
    main()