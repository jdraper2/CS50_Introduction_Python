import sys

def main():

    line_count = 0
    try:
        with open(check_file(sys.argv)) as file:
            for line in file:
                line = line.strip()
                if line.isspace() == True:
                    pass
                elif len(line) > 0 and line[0] == "#":
                    pass
                elif len(line) == 0:
                    pass
                else:
                    line_count += 1

        with open(check_file(sys.argv)) as file:
            #print(line_count)
            line_count = line_count - (check_multi_line(file))

        print(line_count)
    except FileNotFoundError:
        print("File not found")

def check_multi_line(file):

    start = 0
    finish = 0
    count = 0
    check = 0
    total_comments = 0

    for line in file:
        count += 1
        if "'''" in line and check == 0:
            start = count
            check = 1
        elif "'''" in line and check == 1:
            finish = count
            check = 0
            total_comments = total_comments + (finish - (start - 1))
            #print(f"{total_comments} = {finish} - {start}")

    return total_comments



def check_file(arg):
    if len(arg) == 2:
        try:
            file_name = arg[1].split(".")
            if len(file_name) < 2 or file_name[1] != "py":
                print( "Not a Python file")
            else:
                return file_name[0] + "." + file_name[1]
        except ValueError:
            print("Not a Python file")
    elif len(arg) == 1:
        print("Too few command-line arguments")
    else:
        print("Too many command-line arguments")

    sys.exit(1)



if __name__ == "__main__":
    main()
