def findMinimalProductSumDivision(n):
    '''
    Find all product-sum numbers within 2~n, using a division tree
    This function is used to evaluate the execution time of findProductSum()
    '''
    #recur(2,2,0,0)
    #recur(2,3,0,0)
    #recur(2,4,0,0)
    #recur(2,5,0,0)
    #recur(2,6,0,0)
    #     ,,,
    #recur(2,16,0,0)

    def recur(min, number, currentSum, depth):
        for i in range(min, number+1):
            if number % i == 0:
                sequence[depth] = i
                #sequence[0]=2
                #sequence[1]=3
                #number==i => 끝 노드인지 판별
                #number가 피제수, i가 나누는 수
                if depth>=1 and number == i:                    
                    numFactors = depth + 1 + dividend - (currentSum+i)
                    if numFactors not in dictionary: dictionary[numFactors] = dividend     
                    #dictionary[2]=4     
                             
                recur(i, int(number/i), currentSum+i, depth+1)
                #다음 recur에는 방금 나눴던 i보다 큰 수(즉, 오름차순)으로 하기 위해 min에 i를 전달해준다.
                #recur(나누는 수 오름차순, 몫, 합, 뎁스)
                #recur(2,3,2,1)

    assert type(n)==int and n > 0, f"n={n} must be an integer greater than 0"    
    #maxProduct=16
    maxProduct = n**2
    sequence = [0 for _ in range(maxProduct)]
    dictionary = {}   # (key,value) = (# of factors (k), minimal product-sum number found so far)

    

    for dividend in range(2, maxProduct+1):
        recur(2, dividend, 0, 0)

    result = []    
    for i in range(2,n+1):
        result.append(dictionary[i])
    return result

print(findMinimalProductSumDivision(4))