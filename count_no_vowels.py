# program to count the number of vowels in a word 
word = "programming"
count = 0
for char in word:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count)

# program to count the number of consonants in a word 
word = "programming"
count = 0
for char in word:
    if char.lower() not in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count)