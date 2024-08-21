"""
This module contains functions for calculating factorials.
"""
import time

final_list = []

def factorial(n):
    """
    Calculate the factorial of a given number.

    Parameters:
    n (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the number.
    """

    time.sleep(.1)

    factorial_number = 1

    for i in range (1,n+1):
        factorial_number = factorial_number * i

    return factorial_number

def sum_factorial():
    """
    Print the factorial of a non-negative integer n.
    
    :param n: Non-negative integer
    """

    for i in range(5):

        final_list.append(factorial(i))

    result=sum(final_list)

    print(f"The factorial of {final_list} is {result}")

    return result

if __name__ == "__main__":

    sum_factorial()
