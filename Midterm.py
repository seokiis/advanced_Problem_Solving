import timeit


def MthPrimeFactorizationBelowN(n, m):
    def primeSieve(n):
        primes = [True] * (n+1)
        primes[0] = False
        primes[1] = False

        for i in range(2, int(n**0.5)+1):
            if primes[i]:
                for j in range(i*i, n+1, i):
                    primes[j] = False

        return [i for i in range(2, n+1) if primes[i]]

    def findAnswer(n):
        def recur(minIndex, number, depth):
            for i in range(minIndex, lastIndex):
                product = primes[i]
                if number * product <= n:
                    sequence[depth] = product
                    if depth >= 1:
                        result.append(
                            (sequence[0:depth+1], product*number))
                    recur(i, number*product, depth+1)

        # 최대
        sequence = [0 for _ in range(n)]
        result = []
        recur(0, 1, 0)

        return result

    primes = primeSieve(100)
    lastIndex = len(primes)

    answerArray = findAnswer(n)
    answerArray.sort(key=lambda x: x[1])
    return answerArray[m-1][0]


def speedCompare(n, m):
    numbersWithMoreThanTwoFactors = 0
    for k in range(4, n+1):
        result = []
        quotient = k
        while quotient % 2 == 0:
            quotient /= 2
            result.append(2)

        p = 3
        while p*p <= quotient:
            while quotient % p == 0:
                quotient /= p
                result.append(p)
            p += 2

        if quotient > 2:
            result.append(int(quotient))

        if len(result) >= 2:
            numbersWithMoreThanTwoFactors += 1
            if numbersWithMoreThanTwoFactors == m:
                return result


if __name__ == "__main__":
    print("Correctness test for MthPrimeFactorizationBelowN()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    correct = True

    if MthPrimeFactorizationBelowN(9, 3) == [2, 2, 2]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if MthPrimeFactorizationBelowN(20, 7) == [2, 7]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if MthPrimeFactorizationBelowN(100000, 100) == [7, 19]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if MthPrimeFactorizationBelowN(100000, 4000) == [5, 5, 5, 37]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if MthPrimeFactorizationBelowN(100000, 90000) == [2, 2, 2, 2, 2, 3, 17, 61]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if MthPrimeFactorizationBelowN(1000000, 100) == [7, 19]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if MthPrimeFactorizationBelowN(1000000, 900000) == [2, 2, 2, 23, 5309]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    print()
    print()
    print("Speed test for MthPrimeFactorizationBelowN()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    if not correct:
        print("fail (since the algorithm is not correct)")
    else:
        repeat = 1
        n, m = 100000, 90000
        tSpeedCompare = timeit.timeit(
            lambda: speedCompare(n, m), number=repeat)/repeat
        tSubmittedCode = timeit.timeit(
            lambda: MthPrimeFactorizationBelowN(n, m), number=repeat)/repeat
        print(f"For input n, m: {n}, {m}")
        print(
            f"Average running times of the submitted code and speedCompare: {tSubmittedCode:.10f} and {tSpeedCompare:.10f}")
        if tSubmittedCode < tSpeedCompare:
            print("pass")
        else:
            print("fail")
        print()

        repeat = 1
        n, m = 100000, 4000
        tSpeedCompare = timeit.timeit(
            lambda: speedCompare(n, m), number=repeat)/repeat
        tSubmittedCode = timeit.timeit(
            lambda: MthPrimeFactorizationBelowN(n, m), number=repeat)/repeat
        print(f"For input n, m: {n}, {m}")
        print(
            f"Average running times of the submitted code and speedCompare: {tSubmittedCode:.10f} and {tSpeedCompare:.10f}")
        if tSubmittedCode < tSpeedCompare:
            print("pass")
        else:
            print("fail")
        print()

        repeat = 5
        n, m = 1000000, 100
        tSpeedCompare = timeit.timeit(
            lambda: speedCompare(n, m), number=repeat)/repeat
        tSubmittedCode = timeit.timeit(
            lambda: MthPrimeFactorizationBelowN(n, m), number=repeat)/repeat
        print(f"For input n, m: {n}, {m}")
        print(
            f"Average running times of the submitted code and speedCompare: {tSubmittedCode:.10f} and {tSpeedCompare:.10f}")
        if tSubmittedCode < tSpeedCompare:
            print("pass")
        else:
            print("fail")
        print()
