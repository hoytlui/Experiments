from art import logo


def add(starting_num, new_num):
    return starting_num + new_num

def subtract(starting_num, new_num):
    return starting_num - new_num

def multiply(starting_num, new_num):
    return starting_num * new_num

def divide(starting_num, new_num):
    return starting_num / new_num


def calculate():
    print(logo)
    
    # create operators dict
    operators = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
    }

    to_continue = True
    starting_num = float(input("Enter a number.\n"))
    while to_continue:
        for k in operators:
            print(k)
        operation = input("Select one of the operators above.\n")
        new_num = float(input("Enter a number.\n"))
        answer = operators[operation](starting_num, new_num)
        print(f"{starting_num} {operation} {new_num} = {answer}")
        
        response = input("Press [space] to restart. Otherwise, press anything to continue.\n")
        # recursion
        if response == ' ':
            to_continue = False
            calculate()
        else:
            starting_num = answer
    

calculate()