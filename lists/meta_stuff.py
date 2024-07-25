# What is the output of the following code fragment?

# define stuff list variable
stuff = [2, 25, 80, 12]

# stuff[0] = 2 defined inside another stuff
# stuff[2] = stuff[3]
# stuff[2] = 12
stuff[stuff[0]] = stuff[3]

# output - stuff = [2, 25, 12, 12]
print(stuff)