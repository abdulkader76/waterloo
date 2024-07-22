# The square numbers are the integers of the form K × K, 
# e.g. 9 is a square number since 3 × 3 = 9. 

# Write a program that reads an integer n from input and outputs all the positive square numbers less than n, one per line in increasing order. 

# For example, if the input is 16, then the correct output would be 

n = int(input())
print(n)

for number in range(1, n):
    if (number**2 >= n):
        break
    print(number**2)
    


