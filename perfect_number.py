def is_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    return sum == n

print(is_perfect(6))


def is_perfect(n):
    if n <= 1:
        return False
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i
    return total == n

print(is_perfect(15))


# perfect number yes or not
n = int(input())
total = 0
for i in range(1, n):
    if n % i == 0:
        total += i

if total == n:
    print("Yes")

else:
    print("No")