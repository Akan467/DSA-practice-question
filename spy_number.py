# spy number stands for sum or product sum of a digit == product of the digit

def isSpy(n):
    sum = 0
    product = 1
    while n > 0:
        digit = n % 10
        sum = sum + digit
        product = product * digit
        n = n // 10
    if sum == product:
        return True
    else:
        return False

isSpy(1412)
