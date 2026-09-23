n = int(input())
words = []
for i in range(n):
    words.append(input().strip())

words.sort()
for w in words:
    print(w)