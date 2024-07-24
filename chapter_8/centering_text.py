# For this program, the first line of input is an integer width. Then, there are some lines of text; the line "END" indicates the end of the text. For each line of text, you need to print out a centered version of it, by adding periods .. to the left and right, so that the total length of each line of text is width. (All input lines will have length at most width.) Centering means that the number of periods added to the left and added to the right should be equal if possible; if needed we allow one more period on the left than the right. For example, for input 

total_width = int(input())

while True:
    word = input()
    if word == "END":
        break
    if ((total_width - len(word)) % 2 == 0):
        left_width = int((total_width - len(word)) // 2)
        right_width = int((total_width - len(word)) // 2)
    else:
        left_width = int((total_width - len(word)) // 2) + 1
        right_width = int((total_width - len(word)) // 2)
    
    print(left_width * "." + word + 
        right_width * ".")
    print(len(left_width * "." + word + right_width * "."))
    