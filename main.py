# class Car:
#     def __init__(self , n):
#         self.name = n
#         print(f"my car's name {n}")
#     def test(self):
#         print(f"test {self.name}")
#
# pride = Car("pride 111")

#____________________________________________________________

class A:
    def printA(self):
        print("Inheritance in Python A")
class B(A):
    def printB(self):
        print("Inheritance in Python B")

x = B()
x.printA()
