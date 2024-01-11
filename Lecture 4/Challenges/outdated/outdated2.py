# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

# structure of program
# 1. get date input
# 2. check valid date
# 3. print date

def main():

    while True:
        try: 
            date_input = input("Date: ").strip()
            if check_date(date_input) == True:
                break
        except ValueError:
            pass
        except EOFError:
            return True

def check_date(d):

    if d[0].isnumeric() == True:
        d = d.split("/")
        d = check_month_numeric(d)
        print(d)
        if d == False: 
            return False
    
    elif d[0].isalpha() == True:
        d = d.split()
        d = check_month_alpha(d)
        if d == False:
            return False

    d = check_year(d)
    if d == False:
        return False
    
    d = check_day(d)
    if d == False:
        return False
    
    print_date(d)
    return True

def check_month_numeric(d): 
    
    if int(d[0]) <= 12:
        
        if len(d[0]) < 2 and int(d[0]) < 10:
            d[0] = "0" + d[0]
            return d
        else:
            return d
    else:
        return False

def check_month_alpha(d):
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    
    if d[0].capitalize() in months:
        if int(months.index(str(d[0]).capitalize())) < 9:
            d[0] = str((int(months.index(str(d[0]).capitalize()))+1))
            d[0] = "0" + d[0]
            return d
        else:
            d[0] = str((int(months.index(str(d[0]).capitalize()))+1))
            return d
    else:
        return False


def check_year(d):
    if len(d[2]) <= 4:
        return d
    else:
        False

def check_day(d):
    d[1] = str(d[1]).replace(",", "")

    if len(d[1]) < 2 and int(d[1]) < 10:
        d[1] = "0" + d[1]
        return d
    else:
        return d



def print_date(d):

    print(d[2] + "-" + d[0] + "-" + d[1])

main()