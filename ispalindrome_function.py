def is_palindrome(word):

    return word == word[::-1]

word = input().strip().lower()
print('Yes' if is_palindrome(word) else 'No')