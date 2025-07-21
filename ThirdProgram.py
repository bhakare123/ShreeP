# Write Python program to Accept the base and height of triangle and compute the area
# def calculate_area(base, height):
#     area = 0.5 * base * height
#     return area
#
# base = float(input("Enter the base of the triangle: "))
# height = float(input("Enter the height of the triangle: "))
#
# result = calculate_area(base, height)
#
# print("Area of the triangle is:", result)


# Write python program to compute the future value of specified principal amount, rate of interest and a number of years

# def compute_future_value(principal, rate, years):
#     future_value = principal * (1 + rate) ** years
#     return future_value
#
# principal = 0
# rate = 0
# years = 0
# while principal <= 0:
#     principal = float(input("Enter the principal: "))
#     if principal <= 0:
#         print("Please enter a positive number")
# while rate <= 0:
#     rate = float(input("Enter the annual interest rate (in %): ")) / 100
#     if rate <= 0:
#         print("Please enter a positive number")
#
# while years <= 0:
#     years = int(input("Enter the number of years: "))
#     if years <= 0:
#         print("Please enter a positive number")
#
# result = compute_future_value(principal, rate, years)
# print("Future value after", years, "years is:", round(result, 2))

# Write python program to create all possible permutation from a given collection of distinct numbers

# def get_permutations(String , i = 0):
#
#     if i == len(String):
#         print("".join(String))
#
#     for j in range(i, len(String)):
#
#         words = [c for c in String]
#         words[i], words[j] = words[j], words[i]
#
#         get_permutations(words, i + 1)
#
# print(get_permutations("Shr", 0))

# def generate_permutations(nums):
#     result = []
#
#     def backtrack(path, remaining):
#         if not remaining:
#             result.append(path)
#             return
#         for i in range(len(remaining)):
#             backtrack(path + [remaining[i]], remaining[:i] + remaining[i+1:])
#
#     backtrack([], nums)
#     return result
#
# nums = list(map(int, input("Enter distinct numbers separated by space: ").split()))
#
# perms = generate_permutations(nums)
# print("All possible permutations:")
# for p in perms:
#     print(p)

#
# import time
# def timer(time_sec):
#     while time_sec:
#         minutes, seconds = divmod(time_sec, 60)
#         timeformat = "{:02d}:{:02d}".format(minutes, seconds)
#         print(timeformat )# end='\r', flush=True
#         time.sleep(1)
#         time_sec -= 1
#
# timer(10)
# print("Time End")


# str1 = (input("Enter a String: "))
# char = input("Enter a character to count: ")[0]
# count = 0
#
#
# for i in str1:
#    if i == char:
#       count = count + 1
#
# print(count)

list1 = [1,2,3,3,2,1,5]
print(list(set(list1)))


list2 = [1,2,3,3,2,1,5]
list3 = [1,2,3,3,2,1,6]

print(list(set(list2) ^ set(list3)))










