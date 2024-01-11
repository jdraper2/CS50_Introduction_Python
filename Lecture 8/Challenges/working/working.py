import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):

    if work_time := re.search(r"^([0-9]+):?([0-9]+)? (AM|PM)? to ([0-9]+):?([0-9]+)? (PM|AM)?$", s, re.IGNORECASE):

        sh, sm = check_times(work_time.group(1), work_time.group(2), work_time.group(3))
        eh, em = check_times(work_time.group(4), work_time.group(5), work_time.group(6))

        return f"{sh.zfill(2)}" + ":" + sm + " to " + f"{eh.zfill(2)}"  + ":" + em

    if work_time is None:
            raise ValueError()

def check_times(h, m, d):

    if m is not None:
        if int(h) > 12 or int(h) < 1 or int(m) > 59:
            raise ValueError()
    else:
        m = "00"

    if d == "PM" and h != "12":
        h = int(h)  + 12

    if d == "AM" and h == "12":
        h = 0

    return str(h), m

if __name__ == "__main__":
    main()
