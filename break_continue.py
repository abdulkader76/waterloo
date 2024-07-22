# example of break & continue
input_number = int(input())

for i in range(1, input_number):
    if (i // 2 == 0):
        continue
    if (i % 13 == 0):
        break
    print(i)
print('Done')