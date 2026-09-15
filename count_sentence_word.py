# count sentences and words in a given text

def sentenceWord(s):
    sentcount = 0
    wordcount = 0
    inSent = False
    inWord = False
    for ch in s:
        if ch == "." or ch == '!' or ch == '?':
            inSent = False
            inWord = False
        elif ch == " ":
            inWord = False
        else:
            if not inWord and ch.isalpha():
                inWord = True
                wordcount += 1
            if not inSent:
                inSent = True
                sentcount += 1
    return [sentcount, wordcount]

s = "Sentence one. Sentence two! Is this sentence three? Yes, it is."
print("Number of sentences and words:", sentenceWord(s))