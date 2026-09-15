# neon number is a number where the sum of the digits of the square of the number = number

def isNeon(n):
    sq = n * n
    sum = 0
    while sq > 0:
        digit = sq % 10
        sum += digit
        sq //= 10
    return sum == n

print(isNeon(10))
print(isNeon(20))
print(isNeon(9))