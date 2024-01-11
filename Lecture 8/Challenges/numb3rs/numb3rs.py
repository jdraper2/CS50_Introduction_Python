import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):

    if ip_matches := re.search(r"^([0-9]+).([0-9]+).([0-9]+).([0-9]+)$", ip, re.IGNORECASE):

        if int(ip_matches.group(1)) > 255 or int(ip_matches.group(2)) > 255 or int(ip_matches.group(3)) > 255 or int(ip_matches.group(4)) > 255:
            return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
