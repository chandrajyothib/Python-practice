#-------user defined exception------
class Myexception(Exception):
   pass
num=int(input("Enter your age :"))

try:
    if num<18:
       raise Myexception
except Myexception as e:
   print("Not eligible to vote")
else:
   print("Eligible to vote")



# import logging

# logging.basicConfig(filename="abc.txt",level=logging.DEBUG ,filemode="w")
# #logging.basicConfig(filename="abc.txt",level=logging.INFO,filemode="w")
# #logging.basicConfig(filename="abc.txt",level=logging.ERROR,filemode="w")
# #logging.basicConfig(filename="abc.txt",level=logging.WARNING,filemode="w")
# #logging.basicConfig(filename="abc.txt",level=logging.CRITICAL,filemode="w")
# logging.debug("debug msg")
# logging.info("info msg")
# logging.error("error msg")
# logging.warning("warning msg")
# logging.critical("critical msg")
# a=20
# logging.debug(f"Name is Jyo .Age is {a}")

# try:
#    num=int(input('enter a number'))
#    assert (num >=0), "only non negative numbers accepted"
#    print (num)
# except AssertionError as msg:
#    print (msg)



#------multi threading------
# from time import *
# from threading import *

# class hello(Thread):
#    def run(self):
#       for i in range(5):
#          print("hello")
#          sleep(1)
      
# class hi(Thread):
#    def run(self):
#       for i in range(5):
#          print("hi")
#          sleep(1)

# t1=hello()
# t2=hi()
# start=perf_counter()
# t1.start()     #------instead of using actual method we simply using start() method *_* ----
# sleep(0.2)
# t2.start()

# t1.join()
# t2.join()
# end=perf_counter()
# print(f"process time: {round(end-start)}")
   


