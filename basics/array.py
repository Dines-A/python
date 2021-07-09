# type -1
import array 
#before the () we must use array that is the function dont use other variable .
var=array.array('i',[1,2,3,4])
print(var)
# its not working
#type -2
"""
import array as arr
# but you can use arr instead of array . here not working i dont know
a = arr.array('d', [1.1, 3.5, 4.5])
print(a)"""

#type -3 
from array import *
var=array('i',[1,2,3,4])
print(var.buffer_info())

# copy the array as a basic method
var1=var
print(var1)

# array has so many method reffer videos

# i for loop
for i in var1:
    print(i)