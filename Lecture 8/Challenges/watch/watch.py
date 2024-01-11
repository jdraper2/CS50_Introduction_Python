import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    
    if url := re.search(r".+(https?://(?:www\.)?youtube.com/embed/([a-z0-9]+)).+", s, re.IGNORECASE):
        print(url)
        return url.group(1)




if __name__ == "__main__":
    main()