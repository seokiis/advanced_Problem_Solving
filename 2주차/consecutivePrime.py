import timeit


def findPrimes(maxN):
    '''
    Find all primes <= maxN and return them in a list
    '''
    prime = [True for _ in range(maxN+1)]
    prime[0] = prime[1] = False
    p = 2
    while p*p <= maxN:
        if prime[p]:
            prime[p*p::p] = [False] * ((maxN - p*p) // p + 1)
        p += 1

    # result = []
    # for i in range(len(prime)):
    #     if prime[i]:
    #         result.append(i)

    return prime


def binarySearchEQ(numbers, target):
    '''
    Find target in the list numbers
    If the target exists in the list, return its index. Otherwise, return -1
    '''
    def recur(fromIndex, toIndex):
        if fromIndex > toIndex:
            return toIndex

        mid = int((fromIndex+toIndex)/2)
        if numbers[mid] < target:
            return recur(mid+1, toIndex)
        elif numbers[mid] > target:
            return recur(fromIndex, mid-1)
        else:
            return mid - 1

    return recur(0, len(numbers)-1)


def findLongestConsecutivePrimeSum(*sums):
    maxSum = max(sums)
    # 소수 구하기 [true,false]로 이루어짐. **index 0부터임**
    primeArr = findPrimes(maxSum)

    # true만 모음.
    result = []
    for i in range(2, len(primeArr)):
        if primeArr[i]:
            result.append(i)

    # 첫번째 행을 구함
    primeSumFirstRow = []
    sum = 0
    for p in range(maxSum):
        if primeArr[p]:
            sum += p
            primeSumFirstRow.append(sum)

    answer = []

    for sum in sums:
        left_border = 0
        right_border = binarySearchEQ(primeSumFirstRow, sum)
        primeSumCurrentRow = primeSumFirstRow

        row = 0  # 현재 탐색하는 행
        while left_border < right_border:  # 만약 이 조건을 만족한다면, 아래를 반복하며 표의 각 row 차례로 탐색
            # right_border -> left_border 방향으로
            for i in range(right_border, left_border-1, -1):
                if (primeArr[primeSumCurrentRow[i]]):  # 소수
                    find = (primeSumCurrentRow[i], i+1)  # sum,길이 저장
                    left_border = i+1
                    break  # 다음 row 살핌
            # nextRow update
            row += 1
            primeSumCurrentRow = primeSumCurrentRow[1:]
            for i in range(len(primeSumCurrentRow)):
                primeSumCurrentRow[i] = primeSumCurrentRow[i]-result[row-1]

            right_border = binarySearchEQ(primeSumCurrentRow, sum)

        answer.append(find)

    return answer


def speedCompare1(*sums):
    '''
    Compute the entire 2D table in advance
    This function is used to evaluate the execution time of findLongestConsecutivePrimeSum()
    '''
    maxSum = max(sums)

    prime = [True for _ in range(maxSum)]
    prime[0] = prime[1] = False
    p = 2
    while p*p <= maxSum:
        if prime[p]:
            for i in range(p*p, maxSum, p):
                prime[i] = False
        p += 1

    primeSumFirstRow = []
    sum = 0
    for p in range(maxSum):
        if prime[p]:
            sum += p
            primeSumFirstRow.append(sum)

    primeSums = [primeSumFirstRow]
    for row in range(1, len(primeSumFirstRow)):
        primeSumCurrentRow = []
        for i in range(len(primeSumFirstRow)):
            if i < row:
                primeSumCurrentRow.append(None)
            else:
                primeSumCurrentRow.append(
                    primeSumFirstRow[i] - primeSumFirstRow[row-1])
        primeSums.append(primeSumCurrentRow)


def speedCompare2(*sums):
    '''
    Perform prime sieve for each N in sums
    This function is used to evaluate the execution time of findLongestConsecutivePrimeSum()
    '''
    for sum in sums:
        prime = [True for _ in range(sum)]
        prime[0] = prime[1] = False
        p = 2
        while p*p <= sum:
            if prime[p]:
                for i in range(p*p, sum, p):
                    prime[i] = False
            p += 1

        primeSumFirstRow = []
        sum = 0
        for p in range(sum):
            if prime[p]:
                sum += p
                primeSumFirstRow.append(sum)


if __name__ == "__main__":
    print("Correctness test for findLongestConsecutivePrimeSum()")
    print("For each test case, if your answer does not appear within 5 seconds, then consider that you failed the case")
    correct = True

    if findLongestConsecutivePrimeSum(100, 200, 300) == [(41, 6), (197, 12), (281, 14)]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(500, 600, 700, 800, 900, 1000) == [(499, 17), (499, 17), (499, 17), (499, 17), (857, 19), (953, 21)]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(2000, 5000, 10000, 20000, 50000) == [(1583, 27), (4651, 45), (9521, 65), (16823, 81), (49279, 137)]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(60000, 70000, 80000, 90000, 100000) == [(55837, 146), (66463, 158), (78139, 167), (86453, 178), (92951, 183)]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(1000000, 5000000, 8000000) == [(997651, 543), (4975457, 1150), (7998491, 1433)]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if findLongestConsecutivePrimeSum(10000000) == [(9951191, 1587)]:
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    print()
    print()
    print("Speed test for findLongestConsecutivePrimeSum()")
    if not correct:
        print("fail (since the algorithm is not correct)")
    else:
        repeat = 10
        sums = [5000]
        tSpeedCompare1 = timeit.timeit(
            lambda: speedCompare1(*sums), number=repeat)/repeat
        tSubmittedCode = timeit.timeit(
            lambda: findLongestConsecutivePrimeSum(*sums), number=repeat)/repeat
        print(f"For input sums: {sums}")
        print(
            f"Average running times of the submitted code and the code that computes the entire 2D table in advance: {tSubmittedCode:.10f} and {tSpeedCompare1:.10f}")
        if tSubmittedCode < tSpeedCompare1:
            print("pass")
        else:
            print("fail")
        print()

        sums = [10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000]
        tSpeedCompare2 = timeit.timeit(
            lambda: speedCompare2(*sums), number=repeat)/repeat
        tSubmittedCode = timeit.timeit(
            lambda: findLongestConsecutivePrimeSum(*sums), number=repeat)/repeat
        print(f"For input sums: {sums}")
        print(
            f"Average running times of the submitted code and the code that performs sieve for each sum in sums: {tSubmittedCode:.10f} and {tSpeedCompare2:.10f}")
        if tSubmittedCode < tSpeedCompare2:
            print("pass")
        else:
            print("fail")
