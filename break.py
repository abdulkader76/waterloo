# example of break statement
counter = 0
while True:
    line_in = input()
    if line_in == 'END':
        break
    counter = counter + 1
    print("line", counter, "=", line_in)