import sys
import csv
from tabulate import tabulate

def main():
    
    pizza_menu = []
    try:   
        with open(check_file(sys.argv)) as file:
            reader = csv.DictReader(file)

            for row in reader:
                if sys.argv[1] == "regular.csv":
                    pizza_menu.append({"Regular Pizza": row["Regular Pizza"], "Small": row["Small"], "Large": row["Large"]})
                else:
                    pizza_menu.append({"Sicilian Pizza": row["Sicilian Pizza"], "Small": row["Small"], "Large": row["Large"]})

        print(tabulate(pizza_menu,tablefmt="grid",headers="keys"))

    except FileNotFoundError:
        print("File not found")


    
    


def check_file(arg):
    if len(arg) == 2:
        try:
            file_name = arg[1].split(".")
            if len(file_name) < 2 or file_name[1] != "csv":
                print( "Not a Python file")
            else:
                return file_name[0] + "." + file_name[1]
        except ValueError:
            print("Not a CSV file")
    elif len(arg) == 1:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")

    sys.exit(1)



if __name__ == "__main__":
    main()
