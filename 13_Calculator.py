def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def divide(number1, number2):
    return number1 / number2


def multiply(number1, number2):
    return number1 * number2


def print_menu():
    print('\t1. Add')
    print('\t2. Subtract')
    print('\t3. Multiply')
    print('\t4. Divide')


def validate_inp(in_message, func, caster):
    end = False
    while not end:
        input_val = input(in_message)
        if func(input_val):
            if caster == int:
                return int(input_val)
            elif caster == float:
                return float(input_val)


def valid_operation(operation):
    return operation in ('1', '2', '3', '4')


def is_numeric(number):
    return number.isnumeric()


def get_operation(operation):
    if operation == 1:
        return add
    elif operation == 2:
        return subtract
    elif operation == 3:
        return multiply
    elif operation == 4:
        return divide


def main():
    stop = False
    while not stop:
        print_menu()
        operation = validate_inp('Select choice from 1 to 4:', valid_operation, int)
        number1 = validate_inp('Enter the first operand. Must be a number: ', is_numeric, float)
        number2 = validate_inp('Enter the second operand. Must be a number: ', is_numeric, float)
        func = get_operation(operation)
        print('The result is: {0}'.format(func(number1, number2)))
        stop_program = input('Want to calculate something else?: Y/N')
        if stop_program.upper() == 'N':
            stop = True


main()
