n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
print("numbers: ", numbers)

avg = sum(numbers) / len(numbers)
print("Average: ", avg)
count = 0
for x in numbers:
    
    if x > avg:
        count += 1

print("Above average: " + str(count))