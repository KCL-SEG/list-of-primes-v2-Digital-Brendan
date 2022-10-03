"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def is_prime(n):
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    i = 5
    stop = int(n**0.5)
    while i <= stop:
        if not n%i or not n%(i + 2):
            return False
        i += 6
    return True

def primes(number_of_primes):
    if number_of_primes < 1:
        raise ValueError("number_of_primes must be >= 0")

    list = []

    i = 0
    while len(list) < number_of_primes:
        if is_prime(i):
            list.append(i)
        i += 1

    return list