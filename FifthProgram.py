# from abc import ABC, abstractmethod
#
# class Bank(ABC):
#     @abstractmethod
#     def m1(self):
#         pass
#     def m2(self):
#         print("Hey all")
#
#
# class Bank1(Bank):
#     def m1(self):
#         print("m1")
# obj = Bank1()
# obj.m1()
# obj.m2()

def toptent():
    n=1
    while n <= 10:
        sq = n*n
        yield sq
        n += 1

values = toptent()
for i in values:
    print(i)