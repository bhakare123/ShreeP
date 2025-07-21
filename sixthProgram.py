# import re
#from lib2to3.pygram import pattern_grammar

# class Digya:
#     def search(self):
#         text ="on 2023-07-12 the conference will begin, The event will end on 2023-07-17"
#
#         date_pattern = re.compile(r'(\d{4})-(\d{2})-(\d{2})')
#
#         date = findall(date_pattern, text)
#
#         print(date)
#
#
# obj=Digya()
# obj.search()


# import re
#
# pattern = "is"
# data = "Python is awesome! and also very use full lang now a day "
#
# data1 = re.search(pattern, data, re.IGNORECASE)
#
# print(data1)
#
# if data1:
#     print("Found it!", data1.group())
# else:
#     print("No match!")


# import re
#
# pattern = re.compile(r"Python",re.IGNORECASE)
# data = "Python is awesome! and also very use full lang now a day "
#
# data1 = re.match(pattern, data)
#
# print(type(pattern))
#
# print(data1)
#
# if data1:
#     print("Found it!", data1.group())
# else:
#     print("No match!")


# import re
# pattern = re.compile(r"ab", re.IGNORECASE)
# data = "abacabnab"
# count = 0
#
# data1 = re.finditer(pattern, data)
#
# print(data1)
# for match in data1:
#     count +=1
#     #print(match , match.group(), match.start(), match.end())
#
# print("Total is = ",count)


# import re
# pattern = re.compile(r'dog|cat',re.IGNORECASE)
# data = "I saw Dog running behind cat and cat climbed but dog could't"
# count = 0
#
# data1 = re.findall(pattern, data)
#
# print(data1)
# for match in data1:
#     count +=1
#     print(match)
#
# print("Total is = ",count)


# import re
#
# pattern  = re.compile(r"bb|CC", re.IGNORECASE)
# data = "bbbcccddd"
#
# data1 = re.findall(pattern, data)
# print(data1)


# import re
#
# pattern = re.compile(r'\d')
# data = "The price is $100 and loss is $143"
#
# data1 = re.finditer(pattern, data)
# for match in data1:
#     print(match , match.group())


# import re
#
# pattern = re.compile(r'[a-zA-Z]')
# data = "The price is $199 and loss is $90"
#
# data1 = re.findall(pattern, data)
# print(data1)

# import re
# pattern = re.compile(r'[^aeiou$\d^]')
# data = "The price is $199 and loss is 90"
#
# data1 = re.findall(pattern, data)
# print(data1)


# Condition = for password 1 contain at least one digit or at least one uppercase letter

# import re
#
# password = input("Enter password: ")
# pattern = re.compile(r'[0-9A-Z]')
#
# if re.findall(pattern, password):
#     print("Password is valid")
# else:
#     print("Password is invalid")


# import re
#
# pattern = re.compile(r'[\s]')
# data = "The price is $199 and loss is $90"
#
# data1 = re.finditer(pattern, data)
#
# for match in data1:
#     print(match.group(), match)


# To find the specific word we can use \b

# import re
#
# data = "The price is $199 and loss is $90"
# pattern = re.compile(r'\bprice\b')
#
# data1 = re.finditer(pattern, data)
#
# for match in data1:
#      print(match.group(), match)


# if we want to check the starting word

# import re
#
# data = "The price is $199 and loss is $90"
# pattern = re.compile(r'\Ahe')
#
# data1 = list(re.finditer(pattern, data))
#
# if data1:
#     print("Match")
#     for match in data1:
#         print(match.group())
# else:
#     print("No Match")


# # if we want to check ending word

# import re
#
# data = "The price is $199 and loss is $90"
# pattern = re.compile(r'1\Z')
#
# data1 = list(re.finditer(pattern, data))
#
# if data1:
#     print("Match")
#     for match in data1:
#         print(match.group())
# else:
#     print("No Match")


#If we to match the dotes(.)

# import re
#
# data = "The price is $199 and loss is $90."
# pattern = re.compile(r'\.')
#
# data1 = list(re.finditer(pattern, data))
#
# for match in data1:
#     print(match)


#If we want to match the [] Saquare brackets

# import re
#
# data = "The price is $199 and [] loss is $90."
# pattern = re.compile(r'\[\]')
#
# data1 = list(re.finditer(pattern, data))
#
# for match in data1:
#     print(match)


#if we want to find the /

# import re
#
# data = "The price is $199 and \ [] loss is $90."
# pattern = re.compile(r"\\")
#
# data1 = list(re.finditer(pattern, data))
#
# for match in data1:
#     print(match)


#Find the date from the data

# import re
#
# data = "Today date is 20-09-2055 and yesterday data is 19-09-2055"
# pattern = re.compile(r'\d{2}-\d{2}-\d{4}')
#
# data1 = list(re.finditer(pattern, data))
#
# for match in data1:
#     print(match)


#Dot represent any character except

# import re
#
# data = "I am Shreedhar Bhakare"
# pattern = re.compile(r'.')
#
# data1 = pattern.findall(data)
# print(data1)


#Plus represent one or more items

# import re

# data = "I am Shreedhar Bhakare"
# pattern = re.compile(r'e+')
#
# data1 = pattern.finditer(data)
# for match in data1:
#     print(match , match.group())

# import re
#
# data = "The mareke is 94, 37, 64, 98, 84, 9999"
# pattern = re.compile(r'\d+')
#
# data1 = re.findall(pattern, data)
# print(data1)

# ******************* Find the email in the data **************
# import re
#
# data = "My email address is bhakareshridhar8@gmail.com or Shreebhakare@gmail.com"
# pattern = re.compile(r'\w+@\w+\.\w+')
#
# email_address = re.finditer(pattern, data)
#
# for match in email_address:
#     print(match , match.group())


# import re
#
# data = "my name is Shreedhar Bhakare"
# pattern = re.compile(r'e*')
#
# data1 = re.findall(pattern, data)
# print(data1)


# import re
#
# data = "abb ac aaabbb aaaabbbcc cc bbb bbbbcccc"
# pattern = re.compile(r'a*b+\w+')
#
# data1 = re.findall(pattern, data)
# print(data1)


# import re
#
# data = "Hello Shridhar Bhakare"
# pattern = re.compile(r'^hello',re.IGNORECASE)
#
# data1 = re.findall(pattern, data)
# print(data1)
#
# if data1:
#     print("Yes")
# else:
#     print("No")



# import re
#
# data = ('''Hello Shridhar Bhakare price us 78788 end the topic 66666
#         "the is the numner us 90900''')
# pattern = re.compile(r'\d{5}$',re.MULTILINE)
#
# data1 = re.findall(pattern, data)
# print(data1)

# if data1:
#     print("Yes")
# else:
#     print("No")


# import re
#
# data = ("Colour and color are same")
# pattern = re.compile(r'colou?r', re.IGNORECASE)
# print(pattern.findall(data))
#
# data1 = re.finditer(pattern, data)
#
# for match in data1:
#     print(match , match.group())

# import re
#
# data = ("The mobile number is 960-496-5845 and 2nd is 9423666467")
# pattern = re.compile(r'\d{3}-?\d{3}-?\d{4}')
# print(pattern.findall(data))
#
# data1 = re.finditer(pattern, data)
#
# for match in data1:
#     print(match , match.group())


# import re
#
# data = ["http://baidu.com/", "https://shree.org/","htttp://baidu.com/"]
# pattern = re.compile(r'https?://\w+\.\w+')
#
# for match in data:
#     if re.match(pattern, match):
#         print("Valid Url", match)
#     else:
#         print("Invalid Url", match)


# import re
#
# data = "i have cat and dog "
# pattern = re.compile(r'cat | dog ')
#
# data1 = re.findall(pattern, data)
# print(data1)


# import re
#
# data = "name is Shridhar Bhakare no is 9604965845 and email is bhakareshridhar8@gmail.c "
# pattern = re.compile(r'\d+ | \w+@\w+\.\w+',re.I)
#
# data1 = re.findall(pattern, data)
# print(data1)



# import re
#
# data = "Hello.Shree"
# pattern = re.compile(r'\w+\.\w+#For matches data', re.VERBOSE)
#
# data1 = re.findall(pattern, data)
# print(data1)



import re

data = "Hello.Shree   "
#pattern = re.compile(r'\w+\.\w+#For matches data', re.VERBOSE)

#data1 = re.findall(pattern, data)
print(data)
