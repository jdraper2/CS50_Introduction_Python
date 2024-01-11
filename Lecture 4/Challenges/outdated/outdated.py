# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like 9/8/1636 or September 8, 1636, wherein the month in the latter might be any of the values in the list below:

def main():

    while True:
        try: 
            date_input = input("Date: ")
            if update_date(date_input) == True:
                break
        
        except ValueError:
            pass

        except EOFError:
            return True
        


def update_date(d):
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
    

    if d[0].isnumeric() == True:
        d = d.split("/")
        if int(d[1]) <= 31 and int(d[0]) <= 12 and len(d[2]) <= 4:
            print(str(d[2]) + "-", end="")
            if int(d[0]) < 10:
                print("0" + str(d[0]) + "-", end="")
                if int(d[1]) <= 10:
                    print("0" + str(d[1]))
                else:
                    print(str(d[1]))
            else:
                print(str(d[0]) + "-", end="")
                if int(d[1]) <= 10:
                    print("0" + str(d[1]))
                else:
                    print(str(d[1]))
            return True
        else:
            return False
        
    elif d[0].isalpha() == True:
        d = d.split()
        if d[0].capitalize() in months:
            #print(months.index(str(d[0]).capitalize()))
            if "," in str(d[1]):
                d[1] = str(d[1]).replace(",", "")
                if int(d[1]) <= 31:
                    print(str(d[2]) + "-" , end="")
                    if int(months.index(str(d[0]).capitalize())) < 9:
                        print("0" + str((int(months.index(str(d[0]).capitalize()))+1)) + "-", end="")
                        if int(d[1]) <= 10:
                            print("0" + str(d[1]))
                        else:
                            print(str(d[1]))
                    else:
                        print(str((int(months.index(str(d[0]).capitalize()))+1)) + "-", end="")
                        #print("0" + str(d[0]) + "-", end="")
                        if int(d[1]) <= 10:
                            print("0" + str(d[1]))
                        else:
                            print(str(d[1]))
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

main()