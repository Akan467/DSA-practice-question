sentence = input().strip()
words = sentence.split()

result = []
for w in words:
    result.append(w[0].upper() + w[1:])
    
print(" ".join(result))