word = input().strip().lower()
counts = [0] * 26
for ch in word:
    if 'a' <= ch <= 'z':
        counts[ord(ch) - ord('a')] += 1

for i in range(26):
    if counts[i] > 0:
        print(chr(i + ord('a')) + ":" + str(counts[i]))