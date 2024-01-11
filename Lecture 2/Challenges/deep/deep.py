def main():
    answer = input("What is the answer to the Great Question of Life, the Universe and Everything? ")
    print(check_answer(answer))

def check_answer(answer):
    if answer.isnumeric() and int(answer) == 42:
        return "Yes"
    elif answer.lower() == "forty two" or answer.lower() == "forty-two":
        return "Yes"
    else:
        return "No"
    
main()