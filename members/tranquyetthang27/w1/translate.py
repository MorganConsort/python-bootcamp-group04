"""W1-4: Translate C++ to Python – Sieve of Eratosthenes.

Difference from C++:
In C++, vectors of bool require explicit initialization and size management.
Python lists are dynamic and support list comprehensions for concise code.
"""


def primes_up_to(n):
    """Return a list of all prime numbers up to n (inclusive)."""
    if n < 2:
        return []
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i in range(2, n + 1) if is_prime[i]]


# Keep the original sieve function for reference
def sieve_of_Eratosthenes(n):
    """Return a boolean list where index i is True if i is prime."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return is_prime
