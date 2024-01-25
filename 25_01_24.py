#--------Multi Threading--
# from threading import * 
#print("Current threading  :: ",current_thread().getName())

#------creating thread without using class------

# def display():
#     for i in range(10):
#         print("executed by child thread")
#     print("Child thread -- ",current_thread().getName())
# t=Thread(target=display)   #creating thread for excuting display ----executed by child class ----remaining code executed by main thread
# t.start()     #starting a thread
# t.join()
# for i in range(5):
#     print("executed by Main thread")
# print("Main thread -- ",current_thread().getName())


#------creating threads with extending Thread class

# from threading import * 
# class MyThread(Thread):
#     def run(self):
#         for i in range(5):
#             print("Child thread")
#         print("Child thread name -- ",current_thread().getName())
# t=MyThread()
# t.start()
# for i in range(5):
#             print("Main thread")
# print("Main thread name -- ",current_thread().getName())

#-------creating threads without extending Thread 
 
# from threading import *

# class test:
#     def m1(self):
#         for i in range(5):
#              print("Child thread")
#         print("Child thread name -- ",current_thread().getName())
# o=test()
# t=Thread(target=o.m1)
# t.start()
# for i in range(5):
#              print("Main thread")
# print("Main thread name -- ",current_thread().getName())


from time import *
from threading import *

def doubles(n):
      for i in n:
        sleep(1)
        print("doubles",2*i)
         
      
def square(n):
      for i in n:
        sleep(1)
        print("square",i*i)
         
n=[2,3,4,5,6]
t1=Thread(target=doubles,args=(n,)) 
t2=Thread(target=square,args=(n,)) 

start=perf_counter()
t1.start()     #------instead of using actual method we simply using start() method *_* ----
sleep(0.2)
t2.start()
print("active threads: ",active_count())
t1.join()
t2.join()
print("Main thread identification number",current_thread().ident)
print("child1 thread identification number",t1.ident)               #-------thread identificcation number
print("child2 thread identification number",t2.ident)
print("active threads: ",active_count())
end=perf_counter()
print(f"process time: {round(end-start)}")

    

    

