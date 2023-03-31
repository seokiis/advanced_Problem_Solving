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

    # print("primeArr:", primeArr)

    # true만 모음.
    result = []
    for i in range(2, len(primeArr)):
        if primeArr[i]:
            result.append(i)

    # print("result", result)

    primeSumFirstRow = []
    sum = 0
    for p in range(maxSum):
        if primeArr[p]:
            sum += p
            primeSumFirstRow.append(sum)
    answer = []

    # print("primeSumFirstRow", primeSumFirstRow)

    for sum in sums:
        left_border = 0
        right_border = binarySearchEQ(primeSumFirstRow, sum)
        primeSumCurrentRow = primeSumFirstRow

        row = 0  # 현재 탐색하는 행
        while left_border < right_border:  # 만약 이 조건을 만족한다면, 아래를 반복하며 표의 각 row 차례로 탐색
            # print(left_border, right_border)
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
            # print("row", row)
            # print("nextRow", primeSumCurrentRow)
            right_border = binarySearchEQ(primeSumCurrentRow, sum)

        answer.append(find)
    # print(answer)

    return answer


findLongestConsecutivePrimeSum(500, 600, 700, 800, 900, 1000)
# findLongestConsecutivePrimeSum(500, 600, 700, 800, 900, 1000) == [(499, 17), (499, 17), (499, 17), (499, 17), (857, 19), (953, 21)]:
