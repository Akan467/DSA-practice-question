# program for length of the longest word in a sentence

def LongestWordLength(str):
    n = len(str)
    res = 0
    current_len = 0
    for i in range(0, n):
        if str[i] != ' ':
            current_len += 1
        else:
            res = max(res, current_len)
            current_len = 0
    return max(res, current_len)

s = "The quick brown fox jumps over the lazy dog"
print("Length of the longest word:", LongestWordLength(s))

# Python program to find the number of characters 
# in the longest word in the sentence. 

def longestWordLength(string):
    
    length = 0
    
    # Finding longest word in sentence
    for word in string.split():
        if(len(word) > length):
            length = len(word)
    
    return length 

# Driver Code
string = "I am an intern at geeksforgeeks"
print(longestWordLength(string))

# This code is contributed by Vivekkumar Singh