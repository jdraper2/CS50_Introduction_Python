import re


def main():
    tweet = input("Input: ")
    print("Output: " + shorten(tweet))


def shorten(word):
    pattern = re.compile('[aeiouAEIOU]')
    result = re.sub(pattern, '', word)
    return result


if __name__ == "__main__":
    main()