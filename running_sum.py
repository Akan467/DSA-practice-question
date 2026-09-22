n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

# print running sum
numbers.sort()
print(numbers)

total = 0
result = []
for x in numbers:
    total += x
    result.append(str(total))

print(' '.join(result))