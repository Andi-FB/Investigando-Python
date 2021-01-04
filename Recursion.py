def divides(number, candidate):
    if number == 1:
        return True
    if candidate % number == 0 or candidate % 2 == 0:
        return False
    else:
        return divides(number-1, candidate)


def is_prime(number):
    print('Is prime?: {}'.format(divides(number - 1, number)))


is_prime(4)
is_prime(5)
is_prime(31)
is_prime(223992)


