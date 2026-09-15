#an ugly number is a positive integer whose only prime factors are 2, 3 or 5 with included 1.

# dynamic programming approach

def isUgly(n):
    arr = [0] * n
    ind2 = 0
    ind3 = 0
    ind5 = 0
    mulTwo = 2
    mulThree = 3
    mulFive = 5
    nextNum = 1
    arr[0] = 1
    for i in range(1, n):
        nextNum = min(mulTwo, mulThree, mulFive)
        arr[i] = nextNum
        if nextNum == mulTwo:
            ind2 += 1
            mulTwo = arr[ind2] * 2
        if nextNum == mulThree:
            ind3 += 1
            mulThree = arr[ind3] * 3
        if nextNum == mulFive:
            ind5 += 1
            mulFive = arr[ind5] * 5
    return nextNum

print(isUgly(10))