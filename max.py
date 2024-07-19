# Code scramble: make the program sort the three numbers 
# x, y and z into increasing order, so that x has the 
# smallest value, y has the next smallest value, and 
# z has the largest value.

# Example variables x, y, z
# replace the variables with any number
x = 300; y = 200; z = 100

tmp = max(x, y)
x = min(x, y)
y = tmp

tmp = max(y, z)
y = min(y, z)
z = tmp

tmp = max(x, y)
x = min(x, y)
y = tmp

print(x)
print(y)
print(z)