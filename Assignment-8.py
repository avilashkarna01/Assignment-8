#Question-1
import time
print(time.gmtime())
print("\n")

#Question-2
import time
print(time.ctime())
print("\n")

#Question-3
import time
print(time.ctime())
print("\n")
a = (time.gmtime())
print("the month from the time  :",a)
print("the month is :",a[1])
print("\n")

#Question-4
import time
t = time.gmtime()
print("the current time is :",time.ctime())
day = t[6]
if day == 0:
	print("monday")
if day == 1:
	print("tueday")
if day == 2:
	print("wednesday")
if day == 3:
	print("thrday")
if day == 4:
	print("friday")
if day == 5:
	print("satday")
if day == 6:
	print("sunday")
print("\n")

#Question-5
import time
t=time.gmtime()
date=t[2]
print("the current date is: ",date)
print("\n")

#Question-6
import time
print(time.localtime())
print("\n")

#Question-7
import math
x = math.factorial(int(input("Enter the number: ")))
print("factorial : ",x)
print("\n")

#Question-8
import math
x = int(input("Enter 1st number : "))
y = int(input("Enter 2nd number : "))
print("GCD is : ",math.gcd(x,y))
print("\n")

#Question-9
import os
print("\n")
print(os.getcwd())
print("\n")
print(os.name)
print("\n")
print(os.listdir())
print("\n")
print(os.environ)
