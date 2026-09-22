def recursive_sum(n):
    if n <= 0:
        return 0
    return n + recursive_sum(n - 1)

n = int(input())
print("Sum: " + str(recursive_sum(n)))