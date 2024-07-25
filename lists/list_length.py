# Getting the length of a list and using it to iterate through the list.

my_list = [3, 12, "pizza", 3, 4]
print("my_list has length", len(my_list))
for i in range(0, len(my_list)):
    print("item at index", i, ":", my_list[i])
