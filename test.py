import math


def gcd(a, b):
    while b != 0:
        if a > b:
            a, b = b, a % b
        else:
            b = b % a
    return a


def rightTriangle2(N):
    def maxNrest(v1, v2, v3):
        '''
        Return v1 ~ v3 as a 3-tuple, such that the 1st element is the max
            and the 2nd and 3rd elements are the rest
        '''
        if v1 >= v2 and v1 >= v3:
            return v1, v2, v3
        elif v2 >= v1 and v2 >= v3:
            return v2, v1, v3
        else:
            return v3, v1, v2

    total = 3*N*N

    # for A in range(1, (N+1)**2 - 1):  # Choose A > O
    #     x1, y1 = A // (N+1), A % (N+1)
    #     if (x1 == y1 and x1 != 0 and y1 != 0):
    #         a = gcd(x1, y1)

    #         c = (x1 ** 2 + y1 ** 2)/y1
    #         d = (x1 ** 2 + y1 ** 2)/x1

    #         e = math.floor((min(math.floor(c), N) - y1) / (x1 / a))
    #         f = math.floor((min(math.floor(d), N) - x1) / (y1 / a))
    #         total += e+f

    #     elif (x1 > y1 and x1 != 0 and y1 != 0):
    #         a = gcd(x1, y1)

    #         c = (x1 ** 2 + y1 ** 2)/y1
    #         d = (x1 ** 2 + y1 ** 2)/x1

    #         e = math.floor((min(math.floor(c), N) - y1) / (x1 / a))
    #         f = math.floor((min(math.floor(d), N) - x1) / (y1 / a))
    #         total += 2*(e+f)
    # print(total)
    for x1 in range(1, N + 1):
        for y1 in range(1, N + 1):
            if x1 == y1:
                a = gcd(x1, y1)

                c = (x1 ** 2 + y1 ** 2)/y1
                d = (x1 ** 2 + y1 ** 2)/x1

                e = math.floor((min(math.floor(c), N) - y1) / (x1 / a))
                f = math.floor((min(math.floor(d), N) - x1) / (y1 / a))
                total += e+f
            if x1 > y1:

                a = gcd(x1, y1)
                c = (x1 * x1 + y1 * y1) // y1
                d = (x1 * x1 + y1 * y1) // x1
                e = (min(c, N) - y1) // (x1 // a)
                f = (min(d, N) - x1) // (y1 // a)
                total += 2 * (e + f)

    print(total)


rightTriangle2(3)


def rightTriangle1(N):
    def maxNrest(v1, v2, v3):
        '''
        Return v1 ~ v3 as a 3-tuple, such that the 1st element is the max 
            and the 2nd and 3rd elements are the rest
        '''
        if v1 >= v2 and v1 >= v3:
            return v1, v2, v3
        elif v2 >= v1 and v2 >= v3:
            return v2, v1, v3
        else:
            return v3, v1, v2

    count = 0
    for A in range(1, (N+1)**2 - 1):  # Choose A > O
        x1, y1 = A // (N+1), A % (N+1)
        for B in range(A + 1, (N+1)**2):  # Choose B > A
            x2, y2 = B // (N+1), B % (N+1)
            lmax, l1, l2 = maxNrest(
                x1**2 + y1**2, x2**2 + y2**2, (x1-x2)**2 + (y1-y2)**2)
            if lmax == l1 + l2:
                count += 1

    return count


print(rightTriangle1(6))
