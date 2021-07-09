# indro
set={1,2,3,4,5}
print(set)

# it has accepted any type of data type value
set1={1,2,3,"python",50.0,True}
print(set1)

#add the value
set1={1,2,3,"python",50.0,True}
set1.add(100)
print(set1)

#update the value
set1={1,2,3,"python",50.0,True}
set1.update({1000})
print(set1)

#remove th value
set1={1,2,3,"python",50.0}
set1.remove('python')
#set1.remove('py')
# you cant remove the value which is not existed it will be error
print(set1)

#discard th evalue from set
set1={1,2,3,"python",5}
#set1.discard(100)
# if you enterd value is not be in set it will not throw the error but removr function throw the error
set1.discard(1)
print(set1)

#copy the set
s1=set1.copy()
print(s1)

#clear the set
s2=set1.copy()
s2.clear()
print(s2)

#delete the set
set1={1,2,3,"python",50.0}
del set1
# it will be an error bcz alreay the set was deleted
#print(set1)

#find the length
set1={1,2,3,"python",50.0}
print(len(set1))

"""
set={1,2,3,4,5}
set1={1,2,3,4,5}
set3=set+set1
pritn(set3)""" #error