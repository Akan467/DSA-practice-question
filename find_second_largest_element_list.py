n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
numbers.sort()
print(str(numbers[-2]))