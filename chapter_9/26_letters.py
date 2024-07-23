# Write a program which does the reverse of the example above: it should take a character as input and output the corresponding number (between 1 and 26). Your program should only accept capital letters. As error-checking, print invalid if the input is not a capital letter.

letter = input()

if ord(letter) - 64 >= 1 and ord(letter) - 64 <= 26:
    print(ord(letter) - 64)
else:
    print('invalid')