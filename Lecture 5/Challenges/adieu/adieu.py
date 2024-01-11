# In a file called adieu.py, implement a program that prompts the user for names, one per line, until the user inputs control-d. Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and, three names with two commas and one and, and names with  commas and one and, as in the below:

# 1. Get names and put in list, allow user to break
# 2. print loop

import inflect

def main():

    p = inflect.engine()

    name_list = []

    while True:
        try:
            name = input("Name: ")
            name_list.append(name)

        except EOFError:
            break
    
    #print(name_list)
    my_list = p.join(name_list)
    print("\nAdieu, adieu, to " + my_list)


if __name__ == "__main__":
    main()