# Define the function prod(L) as before, but this time using the new kind of loop.

def prod(L):
    product = 1
    for i in L:
        product *= i
    
    return product