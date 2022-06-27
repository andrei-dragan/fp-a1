# Solve the problem from the third set here

"""
    Non-UI functions
"""


def find_prime_divisor(composed_number, numbers_in_the_sequence, n):
    """
    Decompose the number, by also counting the numbers added in the sequence based on the divisors obtained
    :param composed_number: The number we want to find prime divisors for
    :param numbers_in_the_sequence: The counter of values already added in the sequence
    :param n: The index of the value we want to find
    :return: A tuple consisting of:
             the new counter - numbers_in_the_sequence, based on the number of divisors added
             the value of the nth number if we find it and -1 otherwise
    """
    d = 2  # we start with the smallest divisor
    while d * d <= composed_number:
        if composed_number % d == 0:  # we found a prime divisor
            while composed_number % d == 0:  # we take all the powers of this prime divisor
                composed_number = composed_number // d
            current_value = d
            numbers_in_the_sequence += 1
            if n == numbers_in_the_sequence:
                return numbers_in_the_sequence, current_value
        d += 1

    if composed_number != 1:  # if it's not 1, there is still a prime divisor greater than the root of composed_number
        current_value = composed_number
        numbers_in_the_sequence += 1
        if n == numbers_in_the_sequence:
            return numbers_in_the_sequence, current_value

    return numbers_in_the_sequence, -1


def find_nth_number(n):
    """
    Returns the nth number of the sequence
    :param n: The given n
    """
    composed_number = 0  # this is the current composed number we are over in the sequence
    numbers_in_the_sequence = 0  # counter for all the values added to the sequence

    while True:
        composed_number += 1
        if composed_number == 1:
            current_value = 1  # the value of the last number added to the sequence
            numbers_in_the_sequence += 1
            if n == numbers_in_the_sequence:
                return current_value
        else:
            decomposed_number_result = find_prime_divisor(composed_number, numbers_in_the_sequence, n)
            if decomposed_number_result[1] == -1:  # we move on and update the counter
                numbers_in_the_sequence = decomposed_number_result[0]
            else:
                return decomposed_number_result[1]


"""
    UI functions
"""


def read_input():
    return int(input("Tell me a number: "))


def print_number(n):
    print(int(find_nth_number(n)))


def start():
    n = read_input()
    print_number(n)


start()
