"""
Aidan Stout
hw10.py
Problem: Series of problems to help me understand how to use loops and bools
I certify that this is entirely my work
"""


def fibonacci(n):
    count = 1
    n1 = 0
    n2 = 1
    if n < 1:
        return None
    elif n == 1:
        return n2
    else:
        while n > count:
            n_term = n1 + n2
            n1 = n2
            n2 = n_term
            count += 1
        return n2


def double_investment(principle, rate):
    interest = 0
    years = 0
    while interest < (2 * principle):
        interest = principle * (1 + rate)
        years += 1
    return years


def syracuse(n):
    sequence = [n]
    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = 3 * n + 1
        sequence.append(n)


def goldbach(n):
    primes = []
    if n % 2 == 0:
        while sum(primes) != n:
            sdfs
    else:
        return None
