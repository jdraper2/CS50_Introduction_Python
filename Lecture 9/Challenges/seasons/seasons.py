import inflect
import datetime
from datetime import date
import sys
import re



def main():
    date = input("Date of Birth: ")
    date = birth_date(date)
    if date == "Invalid Date":
        sys.exit(date)
    else:
        print(date)

def birth_date(d):
    try:
        datetime.date.fromisoformat(d)
        todays_date = (str(date.today())).split("-")
        d = (str(d)).split("-")
        return convert_days(d, todays_date)
    except ValueError:
        return "Invalid Date"


def convert_days(d, t):
    p = inflect.engine()

    delta = date(int(t[0]), int(t[1]), int(t[2])) - date(int(d[0]), int(d[1]), int(d[2]))
    days = re.search(r'\d+', str(delta)).group()

    mins = int(days) * 24 * 60
    words = p.number_to_words(mins, andword="").capitalize()

    return words + " minutes"


if __name__ == "__main__":
    main()
