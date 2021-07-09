# filter using function 
def is_even(n):
        return n%2==0
num=[1,2,3,4,5,6,7,8,9]
# even=list(filter(is_even,num)) list-> would be set ,touple
even=list(filter(is_even,num))
print(even)

#filter using lambda
num1=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda n : n%2==0,num1))
print(even)