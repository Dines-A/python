#tried by me
def fun(a):
    c=1
    while (a>=1):
        c=c*a
        a-=1
    return c
xyz=fun(6)
print(xyz)

#source from motherong
#source from telusko
def fun1(a):
    if a<=1:
        return a
    return a*fun1(a-1)
x1=int(input("Enter the value :"))
aa=fun1(x1)
print(aa)

#source from telusko
def greet():
    print("recursion")

greet()
# function calling using for loop
def greet1():
    print("recursion")

for i in range(100):
    greet1()

#import sys to calculate how many time the function exicuted
#if you use like this it will exicute untill 1000 times ofter it will show error
# to increse the the time of the output use sys 
import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())
i=0
def greet2():
    global i
    i+=1
    print("recursion",i)
    greet2()
greet2()
