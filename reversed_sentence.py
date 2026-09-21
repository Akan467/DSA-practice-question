def reversed_sentence(sentence):
    words = sentence.split()
    reversed_sentence = ' '.join(reversed(words))
    print(reversed_sentence)


sentence = "Hello world! This is a test sentence."
print(reversed_sentence(sentence))

# use slicing
def reverse_words(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    print(" ".join(reversed_words))

sentence = "Hello world! This is a test sentence."
print(reverse_words(sentence))
