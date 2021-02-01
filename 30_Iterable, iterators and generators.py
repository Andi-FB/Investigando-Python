"""
These exercises focuses on the creation of a generator.
Write a prime number generator; you can use the prime number program you
wrote earlier in the book but convert it into a generator. The generator should take a
limit to give the maximum size of the loop you use to generate the prime numbers.
You could call this prime_number_generator().
You should be able to run the following code:

number = input('Please input the number:')
if number.isnumeric():
num = int(number)
if num <= 2:
print('Number must be greater than 2')
else:
for prime in prime_number_generator(num):
print(prime, end=', ')
else:
print('Must be a positive integer')
If the user enters 27 then the output would be:
Please input the number:27
2, 3, 5, 7, 11, 13, 17, 19, 23,

Now create the infinite_prime_number_generator(); this generator
does not have a limit and will keep generating prime numbers until it is no longer used.
You should be able to use this prime number generator as follows:

prime = infinite_prime_number_generator()
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
print(next(prime))
"""


def divides(number, candidate):
    if number == 1:
        return True
    if candidate % number == 0 or candidate % 2 == 0:
        return False
    else:
        return divides(number-1, candidate)


def is_prime(num):
    return divides(num - 1, num)


def prime_number_generator(num):
    val = 2
    while val <= num:
        if is_prime(val):
            yield val
            val += 1
        else:
            val += 1


number = input('Please input the number:')
if number.isnumeric():
    num = int(number)
    if num <= 2:
        print('Number must be greater than 2')
    else:
        for prime in prime_number_generator(num):
            print(prime, end=', ')
else:
    print('Must be a positive integer')