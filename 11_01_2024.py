#---------------FILE HANDLING---------







#---------Read operation----
# x=open("sample.txt",mode="r")
# print(x.read(10))
# print(x.readline())
# print(x.readlines())
# x.close()

#------Write operation------
# y=open("sample.txt",mode="w")
# y.write("hello")
# y.close()


#-----Append operation-----
# a=open("sample.txt",mode="a")
# a.write("xcvjknlkjh")
# a.close()


#-----r+ operation-----
# b=open("sample.txt",mode="r+")
# print(b.readline())
# b.write("welcome to the world of python")
# print(b.readline())




#-----w+ operation-----
# b=open("sample.txt",mode="w+")

# b.write("welcome to the world of python")
# b.seek(0)
# print(b.readline())
# b.close()

#print(b.read(10))




#-----------------EXCEPTIONAL HANDLING-------

# try:
#     a=10
#     #b=2
#     b=0
#     c=a/b
# except:
#     print("Dividend must not equal to zero")
# else:
#     print(c)
# finally:
#     print("Final block")
    
    
# try:
#     a=10
#     #b=2
#     b=0
#     c=a/b
# except TypeError:
#     print("Type error")
# except ValueError:
#     print("Value error")
# except ZeroDivisionError:
#     print("Dividend must not equal to zero")





#---raise error---
#i=10
i=-1
if i<0:
    raise Exception("Sorry, value must be greater than zero") 
else:
    print(i,"greater than zero")
    

    
