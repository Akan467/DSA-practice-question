# for example: 234 = 2 * 3 * 4 = 24

n = int(input())

if n == 0:
    print(0)
else:
    product = 1
    while n > 1:
        product *= n % 10
        n //= 10
    print(product)