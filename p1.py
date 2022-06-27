# Solve the problem from the first set here

"""
    Non-UI functions
"""


def check_divisor(x):
    """
    Check if x has a divisor between 2 and (x-1)
    :param x: The x we are checking.
    :return: 1 if it has, 0 otherwise
    """
    for i in range(2, x):
        if x % i == 0:  # it means the number has a divisor different from 1 or x => is not prime
            return 1

    return 0


def is_prime(x):
    """
    Check if x is prime
    :param x: The x itself. We treat x = 0, 1, 2 separately
    :return: 1 if prime, 0 otherwise
    """
    if x == 0 or x == 1:
        return 0
    elif x == 2:
        return 1
    else:
        if check_divisor(x) == 1:
            return 0
        else:
            return 1


def find_prime(n):
    """
    Finds the first prime number larger than a given n
    :param n: The given n
    :return: The first prime number
    """
    i = n + 1  # we start with the immediate larger number than n -> (n+1)

    while True:  # as long as this while is True, we didn't find that first prime number
        if is_prime(i):
            return i
        i = i + 1


"""
    UI functions
"""


def read_input():
    return int(input("Enter a number: "))


def print_result(n):
    print(find_prime(n))


def start():
    n = read_input()
    print_result(n)


start()
