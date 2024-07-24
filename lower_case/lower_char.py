# The first step is to write a function lowerChar(char) that can return the result of converting a single character char to lower case. It should do the following:

#   if the input character char is a capital letter (between 'A' and 'Z'), it should return the lower-case version of the letter (between 'a' and 'z') in all other cases, it should return the same char which was input.

def lower_char(char):
    if ord(char) > 64 and ord(char) < 91:
        return (chr(ord(char) + 32))
    else:
        return(char)
    
# print(lower_char('z'))
# print(lower_char('H'))

# Strings
# Now, you will write a second function lowerString(string) which will return the result of converting the entire string to lower case, by calling lowerChar on each character. We suggest you do this as follows:

#    first, copy the definition of lowerChar(char) from your solution to the first part then define a second function, lowerString(string)  on the first line inside lowerString, initialize a variable result = "" equal to the empty string use a for loop with i and set result = result + lowerChar(string[i]) finally, return result

def lower_string(string):
    result = ""
    
    for i in string:
        result += lower_char(i)
        
    return result

print(lower_string('Gr3at!'))
print(lower_string('This Is not gonna End Well!'))