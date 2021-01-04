"""The aim of this exercise is to explore higher order functions.
You should write a higher order function function called
my_higher_order_function(i, func). This function takes a parameter
and a second function to apply to the parameter.
15.5 Python Higher Order Functions 165
Now you should write a sample program that uses the higher order function you
just created to perform. An example of the sort of thing you might implement is
given below:
If you are using the above code as your test application then you should write
each of the supporting functions; each should take a single parameter.
Sample output from this code snippet is:
Note a simple way to find the square root of a number is to use the exponent (or
power of) operator and multiply by 0.5.
print(my_higher_order_function(2, double))
print(my_higher_order_function(2, triple))
print(my_higher_order_function(16, square_root))
print(my_higher_order_function(2, is_prime))
print(my_higher_order_function(4, is_prime))
print(my_higher_order_function('2', is_integer))
print(my_higher_order_function('A', is_integer))
print(my_higher_order_function('A', is_letter))
print(my_higher_order_function('1', is_letter))"""


def double(number):
    return number * 2


def triple(number):
    return number * 3


def square_root(number):
    return number ** 0.5


def has_dividers(number, candidate):
    if number == 1:
        return True
    return not modulus(candidate, number) == 0 and has_dividers(minus_one(number), candidate)


def modulus(number1, number2):
    return number1 % number2


def is_even(number):
    return number % 2 == 0


def minus_one(number):
    return number - 1


def is_prime(number):
    return has_dividers(minus_one(number), number)


def my_higher_order_function(param, function):
    return function(param)


def is_integer(param):
    try:
        int(param)
        return True
    except ValueError:
        return False


def is_letter(param):
    return ('a' <= param <= 'z') or ('A' <= param <= 'Z')


print(my_higher_order_function(2, double))
print(my_higher_order_function(2, triple))
print(my_higher_order_function(16, square_root))
print(my_higher_order_function(2, is_prime))
print(my_higher_order_function(4, is_prime))
print(my_higher_order_function('2', is_integer))
print(my_higher_order_function('A', is_integer))
print(my_higher_order_function('A', is_letter))
print(my_higher_order_function('1', is_letter))

# Currying

"""This exercise is about creating a set of functions to perform currency conversions
based on specified rates using currying to create those functions.
Write a function that will curry another function and a parameter in a similar
manner to multby in this chapter—call this function curry().
Now define a function that can be used to convert an amount into another
amount based on a rate. The definition of this conversion function is very straight
forward and just involves multiplying the number by the rate.
Now create a set of functions that can be used to convert a value in one currency
into another currency based on a specific rate. We do not want to have to remember
the rate, only the name of the function. For example:
If the above code is run the output would be:
    dollars_to_sterling = curry(convert, 0.77)
    print(dollars_to_sterling(5))
    euro_to_sterling = curry(convert, 0.88)
    print(euro_to_sterling(15))
    sterling_to_dollars = curry(convert, 1.3)
    print(sterling_to_dollars(7))
    sterling_to_euro = curry(convert, 1.14)
    print(sterling_to_euro(9))"""


def convert(number, ratio):
    return number * ratio


def curry(function, param):
    return lambda number: function(number, param)


dollars_to_sterling = curry(convert, 0.77)
print(dollars_to_sterling(5))
euro_to_sterling = curry(convert, 0.88)
print(euro_to_sterling(15))
sterling_to_dollars = curry(convert, 1.3)
print(sterling_to_dollars(7))
sterling_to_euro = curry(convert, 1.14)
print(sterling_to_euro(9))
