# The words 1st, 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, 9th are called ordinal adjectives. Write a program which reads an integer x between 1 and 9 from input. The program should output the ordinal adjective corresponding to x. 

x = int(input())

if x == 1:
    print(str(x) + 'st')
elif x == 2:
    print(str(x) + 'nd')
elif x == 3:
    print(str(x) + 'rd')
else:
    print(str(x) + 'th')

