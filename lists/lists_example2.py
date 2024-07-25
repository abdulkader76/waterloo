# changing the lists items

my_list = [1, 10, 100, 1000]
for i in range(0, 2):
    my_list[i] = 2 * my_list[i] + i

print(my_list)