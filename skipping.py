# Extend the "Looping through all lines of input" example above (we've copied it for you) by adding a new feature: any line equal to SKIP should not be printed, and should not cause the counter to be increased. Run the program to see an example.
counter = 0
while True:
    line_in = input()
    if line_in == 'SKIP':
        continue
    if line_in == 'END':
        break
    counter = counter + 1
    print("line", counter, "=", line_in)