#  write a python program to read a file and to convert a date of yyyy-mm-dd format to dd-mm-yyyy format

# import re
# from importlib.resources import contents
#
# file_name = input("Enter the file name")
# pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
#
# try:
#     with open(file_name, 'r')as file:
#         contents = file.read()
#
#     converted_contents = pattern.sub(r'\3-\2-\1', contents)
#
#     print("********Converted Contents*************")
#     print(converted_contents)
#
# except FileNotFoundError:
#     print("File not found")
# except Exception as e:
#     print("Error is occure",e)


# Write a python program to match if two words from list of words starting with letter 'p'

# import re
#
# words = ["pen", "apple", "pencil", "banana", "paper"]
#
# pattern = re.compile(r'^p', re.IGNORECASE)
# count = 0
# for word in words:
#     if pattern.match(word):
#         print(word)
#         count += 1
#
# if count >= 2:
#     print("Found at least two words starting with 'p'")
# else:
#     print("Less than two words start with 'p'")


# write a python program to find the occurence and position of the subString within a string

import re

text = input("Enter the main string: ")
sub = input("Enter the substring to search: ")

matches = list(re.finditer(re.escape(sub), text))


if matches:
    print(f"\n Found {len(matches)} occurrence(s) of '{sub}':")
    for match in matches:
        print(f"At index {match.start()} to {match.end() - 1}")
else:
    print(f"\n Substring '{sub}' not found.")
