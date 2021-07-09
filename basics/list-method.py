"""TYPE	   ORDERED	 CHANGEABLE	 DUPLICATE	  indexed
   LIST   	YES	          YES	  YES	       YES        """



# find the length
list=[1,2,3,4,5,6,6,6,6,6]
print(len(list))
print(list)

# concatenating two list
a=['a','b','c']
b=a[:]
print(a+b)

#append th list
a=[1,2,3,4,5,6]
a.append(10)
print(a)

#insert the value
list=[1,2,3,4]
list.insert(0,9)
print(list)

# remove item from list
list=[1,2,3,4,5,6,7,8,9,0]
list.remove(1)
#remove can aceept only one arg
print(list)

#remove item using del 
list=[1,2,3,4]
del list[0]
print(list)

#clear a list
list=[1,2,3,4]
list.clear()
print(list)


#delete the list
list=[1,2,3,4]
del list
print(list)