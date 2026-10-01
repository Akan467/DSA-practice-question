num = input().strip()

counts = [0] * 10
for ch in num:
    if '0' <= ch <= '9':
        counts[int(ch)] += 1

for i in range(10):
    if counts[i] > 0:
        print(str(i) + ":" + str(counts[i]))