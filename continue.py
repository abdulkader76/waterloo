# example of continue statement
n = int(input())

for number in range(10, n):
    if (number % 13 == 0):
        continue
    print(number)
