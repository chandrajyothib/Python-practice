#----------OOPS concepts-------

# class car():
#     a=10
#     print("i am class")
#     def output(self):
#         print(self.a+10)
#         print("i am method ")
# b=car()
# print(b)
# b.output()
# print(b.a)

#----------------Single Inheritance---------

# class parent():
#     def output(self):
#         print("i am parent")
# class child(parent):
#     def outputc(self):
#         print("i am child ")
# a=child()
# a.output()
# a.outputc()


#----------------Multilevel Inheritance---------


# class grandparent():
#     def outputgf(self):
#         print("i am grandparent")
# class parent(grandparent):
#     def output(self):
#         print("i am parent")
# class child(parent):
#     def outputc(self):
#         print("i am child ")
# a=child()
# a.output()
# a.outputc()
# a.outputgf()
# b=grandparent()
# b.outputgf()


# #----------------Multiple Inheritance---------


# class father():
#     def outputgf(self):
#         print("i am father")
# class mother():
#     def output(self):
#         print("i am mother")
# class child(father,mother):
#     def outputc(self):
#         print("i am child ")
# a=child()
# a.outputgf()
# a.output()
# a.outputc()



#----------------Heirarchial Inheritance---------


class parent():
    def output(self):
        print("i am Parent")
class child1(parent):
    def outputc1(self):
        print("i am child1")
class child(parent):
    def outputc(self):
        print("i am child2")
a=child()
b=child1()
a.output()
a.outputc()
b.output()
b.outputc1()
