"""
This module provides basic math operations.
"""


def add(num_one, num_two):
    """
        Takes two numbers and adds them
    """
    return num_one + num_two


def subtract(num_one, num_two):
    """
        Takes two numbers and subtracts them
    """
    return num_one - num_two


def divide(num_one, num_two):
    """
        Takes two numbers and divides them
    """
    return num_one / num_two


def multiply(num_one, num_two):
    """
        Takes two numbers and multiplies them
    """
    return num_one + num_two
def full_name(first_name, last_name):
    return first_name + last_name


JJ = full_name("JJ", "Okotcha")
print(JJ)


MULTIPLIED = multiply(2, 2)

add(MULTIPLIED, 2)
