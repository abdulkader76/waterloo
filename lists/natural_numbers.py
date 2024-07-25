# Write a function naturalNumbers which takes a positive integer n as input, and returns a list [1, 2, ...] consisting of the first n natural numbers.

def natural_numbers(n):
    natural_numbers = []
    for i in range(1, n + 1):
        natural_numbers += [i]
    
    return natural_numbers

nature = natural_numbers(120)
print(nature)
