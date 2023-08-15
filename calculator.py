
def execute(operation,x,y):

    if operation == 1:
        return x + y
    elif operation == 2:
        return x - y
    elif operation == 3:
        return x * y
    elif y == 0:
        return "Undefine: Division by zero"
    else:
        return x / y


def get_number(position, repeat=True):
    #print(position)
    while repeat:
        number = input("Enter the {}: ".format(position))

        try:
            try:
                return int(number)
            except:
                return float(number)
            
        except ValueError:
            repeat = True

def get_operation():
    operation_dict = {"1" : "+", "2" : "-", "3" : "*", "4" : "/"}
    while True:
        operation =  input("Choose an operation:\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division\n")
        if operation in operation_dict.keys():
            break
    return int(operation), operation_dict[operation]

def main():
    first_number = get_number("first number")
    second_number = get_number("second number")

    operation, symbol = get_operation()

    result = execute(operation,first_number,second_number)

    print(f"Result: {first_number} {symbol} {second_number} = {result}")


if __name__ == "__main__":
    main()

