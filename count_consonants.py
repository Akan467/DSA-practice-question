n = input().strip()

count = 0
for c in n:
    if c not in "aeiouAEIOU":
        count += 1

print(count)


