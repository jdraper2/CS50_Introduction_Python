import csv
import sys

def main():

    input, output = check_args(sys.argv)
    try:
        with open(input) as csvfile:
            reader = csv.DictReader(csvfile)

            with open(output, "w") as file:
                writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
                writer.writeheader()

                for row in reader:
                    names = (row["name"]).split(",")
                    first_name = names[1].lstrip()
                    last_name = names[0].lstrip()
                    house = row['house'].lstrip()
                    writer.writerow({"first": first_name, "last": last_name, "house": row['house']})

    except FileNotFoundError:
        sys.exit("File not found")

def check_args(args):

    if len(args) < 2:
        sys.exit("Too few command-line arguments")
    elif len(args) > 3:
        sys.exit("Too many command-line arguments")
    else:
        try:
            in_file = args[1].split(".")
            out_file = args[2].split(".")

            if len(in_file) > 1 and len(out_file) > 1 or in_file[(len(in_file)+1)] == "csv" and out_file[(len(out_file)+1)] == "csv":
                in_file = in_file[0] + "." + in_file[1]
                out_file = out_file[0] + "." + out_file[1]
                if is_csv(in_file) == False:
                    sys.exit("Not a CSV file")
                else:
                    return in_file, out_file
            else:
                sys.exit("Not a CSV file")

        except (IndexError, ValueError):
            sys.exit("Not a CSV File")


def is_csv(file):
    try:
        with open(file, 'r') as f:
            dialect = csv.Sniffer().sniff(f.read(1024))
            f.seek(0)
            reader = csv.reader(f, dialect)
            headers = next(reader)  # Skip the header
    except (csv.Error, FileNotFoundError):
        # If an error is raised, the file is not a CSV
        return False
    # If no error was raised, the file is a CSV
    return True



if __name__ == "__main__":
    main()
