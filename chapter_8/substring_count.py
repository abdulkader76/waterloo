# As mentioned in lesson 7A, a substring is any consecutive sequence of characters inside another string. The same substring may occur several times inside the same string: for example "assesses" has the substring "sses" 2 times, and "trans-Panamanian banana" has the substring "an" 6 times. Write a program that takes two lines of input, we call the first needle and the second haystack. Print the number of times that needle occurs as a substring of haystack.

needle = input()
haystack = input()

needle_length = len(needle)
start = 0
count = 0

for letter in haystack:
    if (haystack[start:needle_length] == needle): 
        count += 1
    
    start += 1
    needle_length += 1

print(count)