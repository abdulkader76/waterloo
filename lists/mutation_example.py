# Error caused by trying to assign a value to a character in a string.

word = 'slack'
print(word, word[1])
word[1] = "n"

# TypeError: 'str' object does not support item assignment