text = input().strip().lower()
count = 0
for ch in text:
    if ch in 'aeiou':
        count += 1

print("vowel:" + str(count))