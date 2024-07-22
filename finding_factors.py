# If a × b = n, we call a × b a factorization of n. In this exercise, write a program that takes a positive integer n from input, and then outputs all factorizations of n; you should follow the formatting given by the following example for n=10.

n = int(input())

# for first_number in range(1, n + 1):
#     for second_number in range(n, 0, -1):
#         if (first_number * second_number == n):
#             print(first_number, 'times', second_number, 'equals', n)

# e.g of first solution with a shorter loop
for number in range(1, n + 1):
    if (n % number == 0):
        print(number, 'times', n // number, 'equals', n)