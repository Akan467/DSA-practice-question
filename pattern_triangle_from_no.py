n = int(input())
for i in range(1, n+1):
    result = []
    for j in range(1, i+1):
        result.append(str(j))
    print(' '.join(result))