def sieve_of_Eratosthenes(n: int) -> list[bool]:
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, n):
        if i == True:
            for j in range(i * i, n, i):
                is_prime[j] = False
    return is_prime
