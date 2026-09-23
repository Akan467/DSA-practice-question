n = int(input())
a, b = 0, 1
result = []
for i in range(n):
    result.append(str(a))
    a, b = b, a + b
print(" ".join(result))


# another way 
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)

sequence = [fibonacci(i) for i in range(n)]
print(sequence)


# another way
def fibonacci(n):
    sequence = [0, 1]
    for i in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

print(fibonacci(8))