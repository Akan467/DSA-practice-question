text = input().strip()
result = ''
for ch in text:
    if not result or ch != result[-1]:
        result += ch

print(result)