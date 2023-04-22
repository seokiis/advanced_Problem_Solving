import math
import timeit
import random


def createProductSumSequence(sequence, maxIndex):
    '''
    Create a product-sum string given a sequence of numbers (e.g., createProductSumSequence([2,3], 2) --> '6=1*2*3=1+2+3')

    Input:
        sequence -- list of integers
        maxIndex -- maximum index to use for sequence (i.e., sequence[0] ~ sequence[maxIndex] are used to create the string)
    '''
    result = []

    product = 1
    sum = 0
    for i in range(maxIndex+1):
        product *= sequence[i]
        sum += sequence[i]

    result.append(f"{product}=")
    for i in range(product-sum):
        result.append("1*")
    for i in range(maxIndex+1):
        result.append(str(sequence[i]))
        if i < maxIndex:
            result.append("*")
    result.append("=")
    for i in range(product-sum):
        result.append("1+")
    for i in range(maxIndex+1):
        result.append(str(sequence[i]))
        if i < maxIndex:
            result.append("+")

    return ''.join(result)


# 자연수 n이 입력으로 주어졌을 때, 2~n 범위에 속하는 모든 product-sum numbers를 찾아 반환.
def findProductSum(n):
    '''
    Find all product-sum numbers within 2~n
    '''
    def recur(min, number, depth):
        for i in range(min, n):
            if number * i <= n:
                sequence[depth] = i
                if depth >= 1:
                    result.append(createProductSumSequence(
                        sequence[0:depth+1], depth))
                recur(i, number*i, depth+1)

    # 최대
    sequence = [0 for _ in range(n)]
    result = []
    recur(2, 1, 0)

    return result


def findMinimalProductSum(n):
    '''
    Find all a minimal product number for each k in 2<=k<=n
    '''

    # proudct가 곱하는 숫자
    def recur(product, number, currentSum, depth):
        for i in range(product, maxProduct//number+1):
            if depth >= 1:
                product = number*i
                # product-currentSum+i == (더해줘야 하는 1의 개수)
                # depth+1 == (1말고 숫자 개수)
                numFactors = depth + 1 + (product) - (currentSum+i)
                if numFactors not in dictionary:
                    dictionary[numFactors] = product
                else:
                    dictionary[numFactors] = min(
                        dictionary[numFactors], product)
            recur(i, number*i, currentSum+i, depth+1)

    # 최대
    maxProduct = n**2
    result = []
    # (key,value) = (# of factors (k), minimal product-sum number found so far)
    dictionary = {}
    recur(2, 1, 0, 0)

    for i in range(2, n+1):
        result.append(dictionary[i])
    return result


def findMinimalProductSumDivision(n):
    '''
    Find all product-sum numbers within 2~n, using a division tree
    This function is used to evaluate the execution time of findProductSum()
    '''
    # recur(2,2,0,0)
    # recur(2,3,0,0)
    # recur(2,4,0,0)
    # recur(2,5,0,0)
    # recur(2,6,0,0)
    #     ,,,
    # recur(2,16,0,0)

    def recur(min, number, currentSum, depth):
        for i in range(min, number+1):
            if number % i == 0:
                sequence[depth] = i
                # sequence[0]=2
                # sequence[1]=3
                # number==i => 끝 노드인지 판별
                # number가 피제수, i가 나누는 수
                if depth >= 1 and number == i:
                    # dividend-(currentSum-i)=추가로 더해줘야하는 1의 개수
                    numFactors = depth + 1 + dividend - (currentSum+i)
                    if numFactors not in dictionary:
                        dictionary[numFactors] = dividend
                    # dictionary[2]=4

                recur(i, int(number/i), currentSum+i, depth+1)
                # 다음 recur에는 방금 나눴던 i보다 큰 수(즉, 오름차순)으로 하기 위해 min에 i를 전달해준다.
                # recur(나누는 수 오름차순, 몫, 합, 뎁스)
                # recur(2,3,2,1)

    assert type(n) == int and n > 0, f"n={n} must be an integer greater than 0"
    # maxProduct=16
    maxProduct = n**2
    sequence = [0 for _ in range(maxProduct)]
    # (key,value) = (# of factors (k), minimal product-sum number found so far)
    dictionary = {}

    for dividend in range(2, maxProduct+1):
        recur(2, dividend, 0, 0)

    result = []
    for i in range(2, n+1):
        result.append(dictionary[i])
    return result


if __name__ == "__main__":
    print("Correctness test for findProductSum()")
    correct = True

    if sorted(findProductSum(4)) == sorted(['4=2*2=2+2']):
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if sorted(findProductSum(6)) == sorted(['4=2*2=2+2', '6=1*2*3=1+2+3']):
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if sorted(findProductSum(9)) == sorted(['4=2*2=2+2', '8=1*1*2*2*2=1+1+2+2+2', '6=1*2*3=1+2+3', '8=1*1*2*4=1+1+2+4', '9=1*1*1*3*3=1+1+1+3+3']):
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if sorted(findProductSum(12)) == sorted(['4=2*2=2+2', '8=1*1*2*2*2=1+1+2+2+2', '12=1*1*1*1*1*2*2*3=1+1+1+1+1+2+2+3', '6=1*2*3=1+2+3', '8=1*1*2*4=1+1+2+4',
                                             '10=1*1*1*2*5=1+1+1+2+5', '12=1*1*1*1*2*6=1+1+1+1+2+6', '9=1*1*1*3*3=1+1+1+3+3', '12=1*1*1*1*1*3*4=1+1+1+1+1+3+4']):
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    if sorted(findProductSum(16)) == sorted(['4=2*2=2+2', '8=1*1*2*2*2=1+1+2+2+2', '16=1*1*1*1*1*1*1*1*2*2*2*2=1+1+1+1+1+1+1+1+2+2+2+2',
                                             '12=1*1*1*1*1*2*2*3=1+1+1+1+1+2+2+3', '16=1*1*1*1*1*1*1*1*2*2*4=1+1+1+1+1+1+1+1+2+2+4', '6=1*2*3=1+2+3',
                                             '8=1*1*2*4=1+1+2+4', '10=1*1*1*2*5=1+1+1+2+5', '12=1*1*1*1*2*6=1+1+1+1+2+6', '14=1*1*1*1*1*2*7=1+1+1+1+1+2+7',
                                             '16=1*1*1*1*1*1*2*8=1+1+1+1+1+1+2+8', '9=1*1*1*3*3=1+1+1+3+3', '12=1*1*1*1*1*3*4=1+1+1+1+1+3+4',
                                             '15=1*1*1*1*1*1*1*3*5=1+1+1+1+1+1+1+3+5', '16=1*1*1*1*1*1*1*1*4*4=1+1+1+1+1+1+1+1+4+4']):
        print("P ", end='')
    else:
        print("F ", end='')
        correct = False

    print()
    print()

    print("Correctness test for findMinimalProductSum()")
    correct = True
    for i in range(10):
        n = random.randint(2, 40)
        if findMinimalProductSum(n) == findMinimalProductSumDivision(n):
            print("P ", end='')
        else:
            print("F ", end='')
            correct = False
            print(
                f"findMinimalProductSum({n}) differs from findMinimalProductSumDivision({n})")
            print(f"findMinimalProductSum({n}): {findMinimalProductSum(n)}")
            print(
                f"findMinimalProductSumDivision({n}): {findMinimalProductSumDivision(n)}")
            print()

    print()
    print()
    print("Speed test for findMinimalProductSum()")
    if not correct:
        print("fail (since the algorithm is not correct)")
    else:
        n = 100
        tSubmittedCode = timeit.timeit(
            lambda: findMinimalProductSum(10), number=n)/n
        tDivSqrt = timeit.timeit(
            lambda: findMinimalProductSumDivision(10), number=n)/n
        print(
            f"Average running time for the submitted code ({tSubmittedCode:.10f}) and the code based on division ({tDivSqrt:.10f})")
        if tSubmittedCode*3 < tDivSqrt:
            print("pass")
        else:
            print("fail")
    print()
