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

    print(len(answerArray))
    print(answerArray)


MthPrimeFactorizationBelowN(100000, 90000)
