#--------multi threading continuation---
# from time import *
# from threading import *

# def doubles(n):
#       for i in n:
#         sleep(1)
#         print("doubles",2*i)
# n=[2,3,4,5,6]
# t1=Thread(target=doubles,args=(n,)) 
# print("Is it daemon thread or not :: ",t1.isDaemon())
# t1.setDaemon(True)
# print("Is it daemon thread or not :: ",t1.daemon)
# t1.start()
# print(t1.name,"is alive: ",t1.isAlive())
# t1.join()
# print(t1.name,"is alive: ",t1.isAlive())
# t=enumerate()
# for i in t:
#     print("Thread name: ",i.name)
#     print("Thread identification: ",i.ident)
# #t1.join()


#----Daemon threads----

# from time import *
# from threading import *

# def m1():
#   print("thread 1")
#   t2=Thread(target=m2)
#   #t2.setDaemon(False)
#   print("is t2 daemon or not :: ",t2.isDaemon())
  
#   t2.start()
# def m2():
#   print("thread 2")
  
# t1=Thread(target=m1)
# t1.setDaemon(True)
# print("is t1 daemon or not :: ",t1.isDaemon())
# t1.start()
# sleep(10)


# #-------Synchronization using lock()----

# from time import *
# from threading import *
 
# def m1(name,age):
  
#    # l.acquire()
#     print("Hii",name)
#     sleep(2)
#     print("Your age is :",age)
#     #l.release()
# l=Lock()
# t1=Thread(target=m1,args=("Jyo",20))
# t2=Thread(target=m1,args=("sai",23))
# t1.start()
# t2.start()


#-------Synchronization using RLock()----

from time import *
from threading import *
 
def fact(num):
    #l.acquire()
    if num<=0:
      result=1
    else:
      result=num*fact(num-1)
          
   # l.release()
    return result
def results(num):
  for i in range(3):
    print("factorial of ",num,"is",fact(num))
  
#l=RLock()
t1=Thread(target=results,args=(5,))
t2=Thread(target=results,args=(3,))
t1.start()
t2.start()
    
