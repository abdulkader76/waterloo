# A palindrome is a word which is spelled the same forwards as backwards. For example, the word 'racecar' is a palindrome: the first and last letters are the same (r), the second and second-last letters are the same (a), etc. Write a function isPalindrome(S) which takes a string S as input, and returns True if the string is a palindrome, and False otherwise.

def is_palindrome(new_string):
    string = new_string
    
    start = 0
    end = -1
    
    while start < len(string):
        if(string[start] != string[end]):
            return False
        start += 1
        end -= 1
    
    return True
        
print(is_palindrome('racecar'))
print(is_palindrome('racenotcar'))
print(is_palindrome('kawanasscsieiubibeui'))
print(is_palindrome('deed'))
