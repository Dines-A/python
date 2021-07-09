# import arthameticfunction file for run this module
"""
this is the content which is existed in arthameticfunction module
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a//b"""
# basic of importing module
# if you just import a function we need to write all time the function  

import arthameticfunction
a=5
b=5
re=arthameticfunction.add(a,b)
print(re)

# using allais
import arthameticfunction as af
a=5
b=5
# if you just import a function we need to write all time the function  
re=af.add(a,b)
print(re)

#importing specify function from module
from arthameticfunction import add
a=5
b=5
re=add(a,b)
print(re)


# importing all properties from that function 
# alla properties a um import pana peraguu andh function la irukara oru function a use panna marandha kuda error varuu
from arthameticfunction import *
a=5
b=5
add=add(a,b)
sub=sub(a,b)
mul=mul(a,b)
div=div(a,b)
print(add)
print(sub)
print(mul)
print(div)