import math


def primeFactorization(n):
    result = []

    if n % 2 == 0:  # Check to see if 2 is a prime factor
        while n % 2 == 0:
            n /= 2
            result.append(2)

    p = 3  # Check to see if odd numbers in 3 ~ sqrt(n) are prime factors
    while p*p <= n:
        if n % p == 0:
            while n % p == 0:
                n /= p
                result.append(3)
        p += 2

    if n > 2:
        # What is left in n must also be a prime factor if n > 2
        result.append(int(n))

    return result


def primeSieve(n):
    primes = [True] * (n+1)
    primes[0] = False
    primes[1] = False

    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False

    return [i for i in range(2, n+1) if primes[i]]


def findSmallestProduct(*n):
    # maxN = max(n)

    primes = primeSieve(100)

    answer = []
    for number in n:
        product = 1
        for prime in primes:
            product *= prime
            if product > number:
                answer.append(product // prime)
                break
    return answer


# if findSmallestProduct(2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == [2, 2, 2, 2, 6, 6, 6, 6, 6, 6]:
#     print("P ", end='')
# else:
#     print("F ", end='')
#     correct = False

# if findSmallestProduct(10000000, 1000000000) == [9699690, 223092870]:
#     print("P ", end='')
# else:
#     print("F ", end='')
#     correct = False


def totientMinimum(*Ns):
    answer = []
    for n in Ns:
        for i in range(n, 1, -1):
            if primeFactorization(i) == [i]:
                answer.append(i)
                break
    return answer


if totientMinimum(2, 3, 4, 5, 6, 7, 8, 9, 10, 11) == [2, 3, 3, 5, 5, 7, 7, 7, 7, 11]:
    print("P ", end='')
else:
    print("F ", end='')
    correct = False
if totientMinimum(50, 500, 1000) == [47, 499, 997]:
    print("P ", end='')
else:
    print("F ", end='')
    correct = False
