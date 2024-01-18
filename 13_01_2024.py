# #----------------Heirarchial Inheritance---------


# class parent():
#     def output(self):
#         print("i am Parent")
# class child1(parent):
#     def outputc1(self):
#         print("i am child1")
# class child(parent):
#     def outputc(self):
#         print("i am child2")
# a=child()
# b=child1()
# a.output()
# a.outputc()
# b.output()
# b.outputc1()


# def square(x):
#     return x*x
# print(square(12.3))


#------------__init__ method-----


class sample():
    def __init__(self):
        print("I am constructor")
    def add(a,b):
        return a+b
z=sample()
print(z.add(3,6))