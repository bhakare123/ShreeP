# class Mobile:
#     def config(self):
#         print("Mobile config")
# a = 19
# a.bit_length()
# print(type(a))
#
# com1 = Mobile()
# Mobile.config(com1)
#
# print(type(com1))
import math
from stringprep import c22_specials


# class com :
#     def __init__(self,cpu, ram):
#         #print("init")
#         self.cpu = cpu
#         self.ram = ram
#
#     def config(self):
#         print("config is",self.cpu, self.ram)
#
#
#
# c1 = com('i5',16)
# c2 = com('Ryzen 3', 8)
#
# c1.config()
# c2.config()

# class Computer:
#     def __init__(self):
#         self.name = "John"
#         self.age = 22
#
#     def comper(self,other):
#         if self.age == other.age:
#             return True
#         else:
#             return False
#
# com1 = Computer()
# com1.age = 22
# com2 = Computer()
#
# if com1.comper(com2):
#     print("They are the same")
# else:
#     print("They are different")


# class Car:
#     wheel = 4
#     def __init__(self):
#         self.mil = 10
#         self.com = 'BMW'
#
# #Name Space is area where you create and store object/variable
# #class namespace
# #object/Instance nameSpace
#
# c1 = Car()
# c2 = Car()
#
# Car.wheel = 10
#
# c1.mil = 20
#
# print(c1.mil, c1.com, c1.wheel)
# print(c2.mil, c2.com, c2.wheel)

# Create a circle class and initialize it with radius. Make two methods getArea and getCircumference this class
#
# class circle:
#     def __init__(self, radius):
#         self.radius = radius
#     def getArea(self):
#         return math.pi * (self.radius ** 2)
#     def getCircumference(self):
#         return 2 * math.pi * self.radius
#
# c = circle(15)
# print(c.getArea())
# print(c.getCircumference())

# class Student:
#     school = "KD"
#     def __init__(self, m1, m2, m3):
#         self.m1 = m1
#         self.m2 = m2
#         self.m3 = m3
#
#     def avg(self):
#         return (self.m1 + self.m2 + self.m3) / 3
#
#     def get_m1(self):
#         return self.m1
#     def get_m2(self):
#         return self.m2
#     def get_m3(self):
#         return self.m3
#
#     def set_m1(self, m1):
#         self.m1 = m1
#     def set_m2(self, m2):
#         self.m2 = m2
#     def set_m3(self, m3):
#         self.m3 = m3
#
#     @classmethod
#     def info(cls):
#         return cls.school
#
#     @staticmethod
#     def info2():
#         print("This is a Static method")
#
#     class laptop:
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i5'
#             self.memory = '4'
#
#         def info(self):
#
#
#
# s1=Student(30,40,10)
# s2=Student(30,40,50)
#
# # print(s1.avg())
# # print(Student.info())
# # Student.info2()
#
# lap1 = Student.laptop()


# class Colg:
#     def __init__(self):
#         print("In a A init")
#     def feture1(self):
#         print("First")
#     def feture2(self):
#         print("Second")
#
# class Colg2(Colg):
#     def __init__(self):
#         super().__init__()
#         print("In a B init")
#     def feture3(self):
#         print("Third")
#     def feture4(self):
#         print("Fourth")
#
# b1 = Colg2()

# class A:
#     def __init__(self):
#        print("In A init")
#     def f1(self):
#         print("First function")
#
# class B:
#     def __init__(self):
#         print("In B init")
#     def f1(self):
#         print("Second function")
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("In C init")
#     def f3(self):
#         print("Third function")
# cc = C()
# cc.f1()

# class AA:
#     def s1(self , name="Shridhar"):
#         print("Welcome " + name + "!")
#
# class BB(AA):
#     def s1(self , name="Shridhar"):
#         print("Not Welcome " + name + "!")
#         super().s1()
#
#
# abj: AA = BB()
# abj.s1()
# abj.s1("Shree")

# class Area:
#     def find_area(self,a=None,b=None):
#         if a!=None and b!=None:
#             print("Area of rectangle = ",a*b)
#         elif a!=None:
#             print("Area of square = ",a*a)
#         else:
#             print("Nothing to do")
#
# obj = Area()
# obj.find_area()
# obj.find_area(2)
# obj.find_area(3,4)








