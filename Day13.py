# Write a Python program for all the cases which can check a string contains only a certain set of characters
import re


def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    string = charRe.search(string)
    return not bool(string)


print(is_allowed_specific_char("ABCDEFabcdef123450"))
print(is_allowed_specific_char("1233@@#$$%$"))


# Write a Python program that matches a word containing 'ab'.
def text_match(text):
    patterns = '\w*ab.\w*'
    if re.search(patterns, text):
        return 'Found a match!'
    else:
        return 'Not matched!'


print(text_match("Python program"))
print(text_match("ababbbabab"))


# Write a Python program to check for a number at the end of a word/sentence.
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False


print(end_num('abcdef12233'))
print(end_num('abcdef634556'))
print(end_num('abc'))

# Write a Python program to search the numbers (0-9) of length between 1 to 3 in a given string
results = re.finditer(r"([0-9]{1,3})", "Exercises number 1, 9, 11, and 222 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))


# Write a Python program to match a string that contains only uppercase letters
    def text_match(text):
        patterns = '^[a-zA-Z0-9_]*$'
        if re.search(patterns, text):
            return 'Found a match!'
        else:
            return 'Not matched!'
print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python_Exercises_1"))
