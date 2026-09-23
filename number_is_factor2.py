n = int(input())

if n <= 0:
    print("No")

else:
    while n > 1:
        if n % 2 != 0:
            break
        n //= 2
    print("Yes" if n == 1 else "No")