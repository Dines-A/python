def fib(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n<0:
        print("enter positive number : ")
    else:
        print(a)
        print(b)
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
            print(c)
i=int(input("Enter the number: "))
fib(i)


#the fibonachi value 

def fib1(n):
    a=0
    b=1
    if n==1:
        print(a)
    elif n<0:
        print("enter positive number : ")
    else:
        print(a)
        print(b)
        for i in range(3,n+1):
            c=a+b
            a=b
            b=c
            if c<=n:
                print(c)
i=int(input("Enter the number: "))
fib1(i)