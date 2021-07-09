def dic(n,d):
    if n<d:
       # n,b=b,n i dont think so
        
        #using theird variable
        a=n+d
        n=a-n
        d=a-d
    #n=n+d
    #d=n-d
    #n=n-d

        print(n/d)
    else:
        print(n/d)

        

n=int(input("enter the value for numerator : "))
d=int(input("enter the value for numerator : "))
dic(n,d)
"""but we have a twist here 
   we have to perform a function without change anything in existing function, assume the function is placed in other file .
"""
def dic1(n,d):
    print(n/d)

def smart_div(func):

    def inner(n,d):
        if n<d:
            n,d=d,n
        return func(n,d)
    return inner

n=int(input("enter the value for numerator : "))
d=int(input("enter the value for numerator : "))

dic1=smart_div(dic1)
dic1(n,d)
