n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))

max_streak = 1
streak = 1
for i in range(1, n):
    if numbers[i] == numbers[i-1]:
        streak += 1
        if streak > max_streak:
            max_streak = streak

    else:
        streak = 1

print("Longest streak: " + str(max_streak))