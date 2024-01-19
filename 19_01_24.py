#------Operator overloading  (overriding predefined operators working)
#-------example1--------
# class A:
#     def __init__(self, a):
#         self.a = a
 
#     # adding two objects 
#     def __add__(self, o):
#         return self.a + o.a 
# ob1 = A(1)
# ob2 = A(2)
# print(ob1 + ob2)


#-------example 2-----
# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def __gt__(self,other):         #predifined methods
#         if(self.age>=other.age):
#             return True
#         else:
#             return False   
# p1=person("Ram",32)
# p2=person("Sita",32)
# # if p1.age>p2.age:
# #     print("P1 will pay bill")
# # else:
# #     print("P2 will pay bill")
# if p1>p2:
#     print("P1 will pay bill")
# else:
#     print("P2 will pay bill")


#-------method overloading------


# class A:
#     def add(self,a=None,b=None,c=None):
#         if(a!=None and b!=None and c!=None):
#             return a+b+c
#         elif(a!=None and b!=None):
#             return a+b
#         else:
#             return a
    

# obj=A()
# print(obj.add(10))
# print(obj.add(10,20))
# print(obj.add(10,20,20))


#---------method overriding------

# class A:
#     def demo(self):
#         print("Class A")
# class B(A):
#     def demo(self):
#         print("Class B")

# # obj=A()
# # obj.demo()
# obj1=B()
# obj1.demo()

#--------Abstract class and Abstract method---
from abc import ABC,abstractmethod

class A(ABC):
    @abstractmethod
    def demo(self):         #---abstract method
        pass
    def sum(self):          #---instance method / normal method
        print("hello")
    
class B(A):
    def demo(self):
        print("Let's go")
        
#obj=A()    #--not possible--
obj=B()
obj.demo()
obj.sum()
    
    




