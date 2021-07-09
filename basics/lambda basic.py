# anonymosh function as called as lambda 
# basic addition
b = lambda a: a+10
print("addition :",b(5))
# basic subraction
b = lambda a: a-10
print("subraction :",b(5))
# basic multiplication
b = lambda a: a*10
print("multiplication :",b(5))
# basic division
b = lambda a: a/10
print("division : ",b(5))
# multipling two value using lambda
b = lambda a,c: a*c
print("a*c : ",b(1,5))
# using all opertor 
c=lambda a,b,c,d:a+b-c*d
print("a+b-c*d : ",c(1,2,3,4))

#lambda in functions
def square(hu):
    return hu*hu
x_yz=square(5)
print("Square is : ",x_yz)

# the above function take so many line let we make reduce the line using lambda

x_yz=lambda a: a*a
ret1=x_yz(5)
print("Square using lambda : ",ret1)




