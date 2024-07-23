# Write a program that takes a single input line of the form «number1»+«number2», where both of these represent positive integers, and outputs the sum of the two numbers. For example on input 5+12 the output should be 17.

S = input()

plus_position = 0
for letter in S:
    if (letter == '+'):
        break
    plus_position += 1
    # print(plus_position)
first_number = S[:plus_position]
# print(first_number)

second_number = S[plus_position + 1:]
# print(second_number)

print(int(first_number) + int(second_number))