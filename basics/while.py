i=1
while i<=10:
      print("the value is  : ",i)
      i+=1


#while with if  statment

i=1
while i<=10:
      if i%2==0:
             print("the value is  : ",i)
      else :
             print("odd value",i)
      i+=1


# when you dont know how many times the statment is going to exiqute you can use at the time 

num=int(input("Enter the number : "))
count=0
while num>1:
       num=num>>1
       #count=count+1
       count+=1
       print(num,count)


#eval is the inbuild function in python
a=eval(input("enter the value : "))
print("the value is " ,a)
