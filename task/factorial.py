def fact(i):
    mul=1
    for i in range(1,i+1):
        mul=mul*i
    print(mul)
i=int(input("enter the value : "))
fact(i)