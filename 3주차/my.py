# n의 모든 인수분해를 출력하는 알고리즘
def factorization(n):
    # recur (몫, 깊이, 나누는 수)
    def recur(output, depth, divisor):
        if (output == 1):
            print(result[0:depth])
            return
        for i in range(divisor, output+1):
            if output % i == 0:
                result[depth] = i
                recur(output//i, depth+1, i)
    result = [0 for _ in range(n)]
    recur(n, 0, 2)


factorization(12)
y
