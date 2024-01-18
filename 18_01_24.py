# import sample


# #---------------__name__---------
# print(__name__)

#------setter and getter methods-----


# class student:
#     def __init__(self):
#         self.age="20"
#     def setter(self,value):
#         self.name=value
#     def getter(self):
#         return self.name,self.age

# s1=student()
# s1.setter("jyo")
# print(s1.getter())

#-------instance method------

# class Cricket:
#     team= None

#     def setTeamName(self, name):
#         self.teamName = name
    
#     def getTeamName(self):
#         return self.teamName

# c = Cricket()
# c.setTeamName('India')
# print(c.getTeamName())

#--------class method------

# class student:
#     clg_name="RGUKT"
#     @classmethod
#     def getClgName(cls):
#         print(cls.clg_name)

# print(student.getClgName())


#-------static method----

# class Cricket:
#     teamName = 'India'  

#     @staticmethod
#     def get_max_value(x, y):
#         return max(x, y)

# c1 = Cricket()
# print(c1.get_max_value(3,6))

#-------method resolution order(multiple inheritance)---


# class A:
#     def __init__(self):
#         print("init of A")
# class B:
#     def __init__(self):
#         print("init of B")
# class C(A,B):
#     def __init__(self):
#         super().__init__()
#         print("init of C")

# a1=C()


#--------Duck typing----

class Duck:
    def quack(self):
        return 'Quack!'

class Person:
    def quack(self):
        return 'I\'m Quacking Like a Duck!'

def in_the_forest(name):
    print(name.quack())

a = Duck()
b = Person()
in_the_forest(a)
in_the_forest(b)

