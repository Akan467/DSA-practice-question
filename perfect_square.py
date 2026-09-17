def isPerfectSquare(num):
    if num < 0:
        return False

    if num == 0:
        return True

    odd = 1
    while num > 0:
        num -= odd
        odd += 2

    return num == 0

print(isPerfectSquare(16))  # Output: True