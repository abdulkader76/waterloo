# Define a function prod(L) which returns the product of the elements in a list L.

def prod(L):
    product = 1
    for i in range(0, len(L)):
        product *= L[i]
    
    return product

print(prod([1, 2, 3, 4, 5]))