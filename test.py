

arr = [0]*101
arr[0] = 1
arr[1] = 1
arr[2] = 2
for i in range(3, 101):
    for j in range(i-1, -1, -1):
        arr[i] += arr[j]*arr[i-j-1]
print(arr)
