# import sample



# #---------------__name__---------
# print(__name__)



#-----------filter() map() reduce() using ananymous function(lambda)----



# l=[1,3,2,4,5,6,7,8]
# evens=list(filter(lambda a:a%2==0,l))
# print(evens)



# l=[1,3,2,4,5,6,7,8]
# double=list(map(lambda n:n*2,l))
# print(double)



# from functools import reduce

# l=[1,3,2,4,5,6,7,8]
# sum=reduce(lambda a,b:a+b,l)
# print(sum)



#-----constructor---


# class student:
#     def __init__(self,name):
#         self.age=18    #default value
#         self.name=name
 
#     # a method for printing data members
#     def print_details(self):
#         print(self.name,self.age)
         
# obj = student("sai")
# obj2 = student("chandu")
# #obj2.name="sai"
# obj.print_details()
# obj2.print_details()


class add:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def display(self):
        print("Number1 : ",self.n1)
        print("Number2 : ",self.n2)
        print("Their sum is : ",(self.n1+self.n2))

obj1=add(10,20)
obj1.display()







