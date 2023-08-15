"""
    Author: Olaoluwa Idowu
    Date: 15-08-23
    Title: PME task1 - calculator
"""


def execute(operation,x,y):    # function to execute operation

    # compute based on the operation seleted

    if operation == 1:
        return x + y
    elif operation == 2:
        return x - y
    elif operation == 3:
        return x * y
    elif y == 0:     # handles division by zero gracefully
        return "Undefine: Division by zero"
    else:
        return x / y


def get_number(position, repeat=True):     # function to request for user's input
    
    while repeat:
        number = input("Enter the {}: ".format(position))

        try:
            # change to int or float
            try:
                return int(number)
            except:
                return float(number)
        # repeat if input is not numeric  
        except ValueError:
            repeat = True


def get_operation():  # function to request operation type from user

    # dictionary to contain operation symbol
    operation_dict = {"1" : "+", "2" : "-", "3" : "*", "4" : "/"}

    # loop to request operation type until options between 1-4 is selected
    while True:
        operation =  input("Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
        if operation in operation_dict.keys():
            break

    # return tuple with operation number and symbol
    return int(operation), operation_dict[operation]


def main():

    # get numbers into variables
    first_number = get_number("first number")
    second_number = get_number("second number")

    # get operation number and operation symbol
    operation, symbol = get_operation()

    # get calcution result
    result = execute(operation,first_number,second_number)

    # print result to standard output
    print(f"Result: {first_number} {symbol} {second_number} = {result}")


# call main function
if __name__ == "__main__":
    main()
