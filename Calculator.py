def add(number1, number2):
    return number1 + number2


def subtract(number1, number2):
    return number1 - number2


def divide(number1, number2):
    return number1 / number2


def multiply(number1, number2):
    return number1 * number2


def main():
    stop = False
    while not stop:
        input_ok = False
        while not input_ok:
            print('\t1. Add')
            print('\t2. Substract')
            print('\t3. Multiply')
            print('\t4. Divide')
            operation = input('Select choice:')
            if operation in ('1', '2', '3', '4'):
                input_ok = True
            else:
                print('Invalid selection')
        input_ok = False
        while not input_ok:
            number1 = input('Enter the first operand. Must be a number: ')
            if number1.isnumeric():
                number1 = float(number1)
                input_ok = True
        input_ok = False
        while not input_ok:
            number2 = input('Enter the second operand. Must be a number: ')
            if number2.isnumeric():
                number2 = float(number2)
                input_ok = True
        operation = int(operation)
        if operation == 2:
            print('The result is: {0}'.format(subtract(number1, number2)))
        elif operation == 1:
            print('The result is: {0}'.format(add(number1, number2)))
        elif operation == 4:
            print('The result is: {0}'.format(divide(number1, number2)))
        elif operation == 3:
            print('The result is: {0}'.format(multiply(number1, number2)))
        stop_program = input('Want to calculate something else?: Y/N')
        if stop_program.upper() == 'N':
            stop = True


main()
