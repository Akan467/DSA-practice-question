# using math in-built 
import math 
def isPerfectSquare(n):
    if n < 0:
        return False
    root = math.sqrt(n)
    return root * root == n

print(isPerfectSquare(16))


# using binary search
def isPerfectSq(n):
    if n < 0:
        return False
    if n <= 1:
        return True
    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        square = mid * mid
        if square == n:
            return True
        if square < n:
            left = mid + 1
        else:
            right = mid - 1
    return False

print(isPerfectSq(25))
print(isPerfectSq(0))
print(isPerfectSq(-4))


# using mathematical Properties - O(sqrt(n))
# perfect square = sum of first few consecutive odd numbers 

def isPerfectSq(n):
    if n < 0:
        return False
    if n == 0:
        return True
    odd = 1
    while n > 0:
        n -= odd
        odd += 2
    return n == 0

print(isPerfectSq(5))