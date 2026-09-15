# automorphic number is a number 
# whose square ends with the same digits as the number 

def isAutomorphic(n):
    sq = n * n
    last = abs(sq) % 10
    if n == last:
        return True
    else:
        return False

print(isAutomorphic(5))
print(isAutomorphic(6))
print(isAutomorphic(25))

# modify for 25 
def isA(n):
    sq = n * n
    digit = len(str(n))
    last = sq % (10 ** digit)
    return n == last

print(isA(25))
