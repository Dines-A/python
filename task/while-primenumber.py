#eval is the inbuild function in python
"""
a=eval(input("enter the value : "))
print("the value is " ,a)
"""
num=int(input("enter the number :  "))
for i in range(2,num):
    if num%i==0:
        print(num,"is not a prime number")
        
        break
else:
    print("yeap this is a prime number",num)
