def sumofdivisior(n):
    sum = 0
    for i in range(1, n+1):
        sum += i * (n//i)
    return sum


print(sumofdivisior(5))