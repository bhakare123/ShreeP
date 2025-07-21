# age = input("Enter your age : ")
# if int(age) >= 18:
#     print("You are old enough")
# else:
#     print("You are not old enough")
#
#
# print("Thank you")


# first_num = int(input("Enter first number: "))
# operators = input("Enter operators (+,-,*,/,%): ")
# second_num = int(input("Enter second number: "))
#
# if operators == "+":
#     print(first_num + second_num)
# elif operators == "-":
#     print(first_num - second_num)
# elif operators == "*":
#     print(first_num * second_num)
# elif operators == "/":
#     print(first_num / second_num)
# elif operators == "%":
#     print(first_num % second_num)
# elif operators == "//":
#     print(first_num // second_num)
# else:
#     print("Invalid operator")


# i = int (1)
#
# while i <= 10 :
#     print(i*"*")
#     i = i + 1
#
# for i in range (6):
#     print(i+1)


# marks = [94, 96, 97, 98 ]
# for mark in marks:
#     print(mark)
#
# marks.append(100)
# print(marks)
#
# marks.insert(0,120)
# print(marks)
#
# # marks.pop()
# # print(marks)
#
# print(12 in marks)
#
# print(len(marks))
#
# i =0
# while i < len(marks):
#     print(marks[i])
#     i += 1
#
# marks.clear()
# print(marks)

# student = ["Shree", "Raj","Susu","Digya","Golu"]
# for std in student:
#     if std == "Digya":
#         continue
#        # break
#     print(std)

# Program to find the factorial of number

# num = int(input("Enter a number : "))
# fact = 1
#
# if num < 0:
#     print("Negative number")
# elif num == 0:
#     print("Factorial of 0 is 1")
# else:
#     for i in range(1,num+1):
#         fact = i*fact
#
# print("Factorial of number is : ",fact)


# marks = (39, 64, 45, 97, 97, 97)
# print(marks)
# print(marks.count(97))
# print(marks.index(97))

# marks = { 29, 30 ,51 ,97, 97, 88}
# print(marks)
# for m in marks:
#     print(m)

# marks = {"English" : 97, "Python" : 67, "java": 98}
# print(marks)
#
# for key, value in marks.items():
#     print(key, value)

# def first_Fun(a , b):
#     print("First function = ",a+b)
#
# first_Fun(10 , 20)

# find out reverse of the number

# num = int(input("Enter a number :"))
# rev = 0
#
# while num > 0:
#     dig = num % 10
#     rev = rev * 10 + dig
#     num = int(num/10)
#
# print("Reversed number is : ",rev)

# Program to check if the input year is a leap or not
# year = int(input("Enter the year"))
#
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print("Leap year ",year)
# else:
#     print("Not Leap year ",year)

# Program to check whether the entered number is prime or not

# num = int(input("Enter a number: "))
# for i in range(2, num+1):
#     if num % i == 0:
#         break
#
# if i == num:
#     print("The number is prime")
# else:
#     print("The number is not prime")

# Program to find sum of the Digit of given number

# n = int(input("Enter a number : "))
# sum = 0
# while n > 0:
#     rem = n % 10
#     sum = sum + rem
#     n =  n // 10
#
# print("Sum of the number : ",sum)



# list = [3, 2, 10, 20, 9, 43, 7, 23]
# print("List",list)
# l=[]
# print("Prime Number from List Are :")
# for a in list:
#     prime = True
#     for i in range(2,a):
#         if a % i == 0:
#             prime = False
#             break
#
#     if prime:
#         l.append(a)
#
# print(l)

# Program to check whether a number is palindrome or not
# num = int(input("Enter a number: "))
# tem = num
# rev = 0
#
# while tem != 0:
#     rev = (rev * 10) + (tem % 10)
#     tem = tem // 10
#
# if num == rev:
#     print("Number is palindrome")
# else:
#     print("Number is not palindrome")

#sum = 0
#cnt = 0

# while True:
#     inp = input("Enter a number: ")
#     if inp == "done":
#         break
#     try:
#         inp = int(inp)
#         cnt += 1
#         sum = sum + int(inp)
#     except:
#         print("Enter a number")
#         continue
#
# avg= sum / cnt
#
# print(avg)
# print(cnt)
# print(sum)

# Write python program to search a specific value from a given list of values using linear search method

# def linear_search(arr, target):
#     for i in range (len(arr)):
#         if arr[i] == target:
#            return i
#     return -1
#
# values = [12, 45, 78, 23, 56, 89, 34]
# target = int(input("Enter value to search : "))
#
# index = linear_search(values, target)
# if index != -1:
#     print(f"Value {target} found at index {index} ")
# else:
#     print(f"Value {target} not found at index {index} ")


# Write python program to search a specific value from a given list of values using binary search method

# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1
#
#     while low <= high:
#         mid = (low + high) // 2
#
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
#
#     return -1
#
#
# values = [12, 23, 34, 45, 56, 78, 89]
# target = int(input("Enter value to search: "))
#
# index = binary_search(values, target)
#
# if index != -1:
#     print(f"Value {target} found at index {index}.")
# else:
#     print(f"Value {target} not found in the list.")

# def sort(num):
#     n = len(num)
#     for i in range(n-1):
#         minps = i
#         for j in range(i,n):
#             if num[j] < num[minps]:
#                 minps = j
#
#         temp = num[i]
#         num[i] = num[minps]
#         num[minps] = temp
#
#         print(num)
#
# num = [50,20,40,10,70]
# sort(num)
# print(num)


# n = {1:"Shree" , 2:"Digya" , 3:"Susu" , 4:"PJ"}
# print(n)
# print(n.get(4))
#
# roll = [1, 2, 3, 4, 5]
# name = ["Deva", "vaishuu", "SG", "KL" , "RP"]
# print(roll)
# print(name)
#
# data = dict(zip(roll, name))
# print(data)
#
# data [9] = "Rajuuu"
# print(data)
#
# del data[3]
# print(data)


dtat1 = {'python':['pycharm','subline'], 'JS':'Atom', 'CS':'Vs', 'Java':{'JES':'Natbeans','JEE':'Eclipse'}}
print(dtat1)
print(dtat1['python'])
print(dtat1['JS'])
print(dtat1['CS'])










